from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("__admin__/", admin.site.urls),
    path("api/auth/", include("authentication.urls")),
    path("api/game/", include("game.urls")),
]
