import json
from typing import TypedDict

from django.contrib.auth import authenticate
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


class UserLoginRequest(TypedDict):
    username: str
    password: str


class UserData(TypedDict):
    username: str
    email: str


class UserLoginResponse(TypedDict):
    user: UserData
    token: str


@csrf_exempt
@require_POST
def login(request: HttpRequest) -> HttpResponse:
    data: UserLoginRequest = json.loads(request.body)
    username = data["username"]
    password = data["password"]
    if not username or not password:
        return JsonResponse(
            {
                "status": "failed",
                "message": "Username and password are required",
            },
            status=400,
        )
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse(
            UserLoginResponse(
                user=UserData(
                    username=user.username,
                    email=user.email,
                ),
                token=token.key,
            )
        )
    else:
        return JsonResponse(
            {
                "status": "failed",
                "message": "Invalid credentials",
            },
            status=400,
        )


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
@require_POST
def logout(request):
    auth_logout(request)
    return JsonResponse(
        {
            "message": "Logged out successfully",
        }
    )
