from typing import Literal, NotRequired, TypedDict

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated

from .engine.game_engine import GameEngine
from .models import GameState as GameStateModel


def get_or_create_latest_game_state(user: User) -> GameStateModel:
    game_state = GameStateModel.objects.filter(user=user).order_by("-created_at").first()
    if not game_state:
        game = GameEngine()
        game_state = GameStateModel.objects.create(user=user, board=game.board, score=game.score)
    return game_state


class GameState(TypedDict):
    board: list[list[int]]
    score: int
    over: bool


class StartNewGameResponse(TypedDict):
    game_state: GameState


class GameStateResponse(TypedDict):
    game_state: GameState


class UserMoveResponse(TypedDict):
    status: Literal["success", "failed"]
    message: NotRequired[str]
    game_state: GameState


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def start_new_game(request: HttpRequest) -> HttpResponse:
    game = GameEngine()
    new_game_state = GameStateModel.objects.create(user=request.user, board=game.board, score=game.score, over=False)
    return JsonResponse(
        StartNewGameResponse(
            game_state=GameState(
                board=new_game_state.board,
                score=new_game_state.score,
                over=new_game_state.over,
            )
        )
    )


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_game_state(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        game_state = get_or_create_latest_game_state(request.user)
        return JsonResponse(
            GameStateResponse(
                game_state=GameState(
                    board=game_state.board,
                    score=game_state.score,
                    over=game_state.over,
                )
            )
        )
    return JsonResponse(
        {
            "error": "Invalid request",
        },
        status=400,
    )


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_move(request: HttpRequest) -> HttpResponse:
    move = request.GET.get("direction")
    game_state = get_or_create_latest_game_state(request.user)

    game = GameEngine()
    game.board = game_state.board
    game.score = game_state.score

    move_result = game.move(move)
    if move_result:
        game_state.board = game.board
        game_state.score = game.score
        game_state.over = game.is_game_over()
        game_state.save()
        return JsonResponse(
            UserMoveResponse(
                status="success",
                game_state=GameState(
                    board=game_state.board,
                    score=game_state.score,
                    over=game_state.over,
                ),
            )
        )
    else:
        game_state.over = game.is_game_over()
        game_state.save()
        return JsonResponse(
            UserMoveResponse(
                status="failed",
                message="Invalid move",
                game_state=GameState(
                    board=game_state.board,
                    score=game_state.score,
                    over=game_state.over,
                ),
            )
        )
