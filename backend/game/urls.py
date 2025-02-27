from django.urls import path

from . import views

urlpatterns = [
    path("move/", views.user_move, name="user_move"),
    path("state/", views.get_game_state, name="get_game_state"),
    path("start/", views.start_new_game, name="start_new_game"),
]
