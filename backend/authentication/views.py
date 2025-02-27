import json
from typing import TypedDict

from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated


class UserData(TypedDict):
    username: str
    email: str


class UserLoginRequest(TypedDict):
    username: str
    password: str


class UserSignupRequest(TypedDict):
    username: str
    password: str
    email: str


class AuthResponse(TypedDict):
    user: UserData
    token: str


class BadRequestResponse(TypedDict):
    error: str
    message: str


@csrf_exempt
@require_POST
def login(request: HttpRequest) -> HttpResponse:
    data: UserLoginRequest = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    if not username or not password:
        return JsonResponse(
            BadRequestResponse(
                error="missing_credentials",
                message="Username and password are required",
            ),
            status=400,
        )
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse(
            AuthResponse(
                user=UserData(
                    username=user.username,
                    email=user.email,
                ),
                token=token.key,
            )
        )
    else:
        return JsonResponse(
            BadRequestResponse(
                error="invalid_credentials",
                message="Invalid credentials",
            ),
            status=400,
        )


@csrf_exempt
@require_POST
def signup(request: HttpRequest) -> HttpResponse:
    data: UserSignupRequest = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    email = data["email"]
    if not username or not password or not email:
        return JsonResponse(
            BadRequestResponse(
                error="missing_credentials",
                message="Username, password, and email are required",
            ),
            status=400,
        )
    User = get_user_model()
    if User.objects.filter(username=username).exists():
        return JsonResponse(
            BadRequestResponse(
                error="username_taken",
                message="Username already exists",
            ),
            status=400,
        )
    user = User.objects.create_user(username=username, password=password, email=email)
    token = Token.objects.create(user=user)
    return JsonResponse(
        AuthResponse(
            user=UserData(
                username=user.username,
                email=user.email,
            ),
            token=token.key,
        )
    )


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
@require_POST
def logout(request: HttpRequest) -> HttpResponse:
    auth_logout(request)
    return HttpResponse(status=204)
