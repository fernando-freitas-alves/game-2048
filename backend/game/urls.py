from django.urls import path

from . import views

urlpatterns = [
    path("move/", views.make_move, name="make_move"),
    path("state/", views.fetch_game_state, name="fetch_game_state"),
    path("new/", views.start_new_game, name="start_new_game"),
]
