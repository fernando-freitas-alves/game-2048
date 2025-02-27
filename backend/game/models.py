import uuid

from django.contrib.auth.models import User
from django.db import models


class GameState(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="game_states")
    board = models.JSONField(default=list)
    score = models.IntegerField(default=0)
    over = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"GameState for {self.user.username} with score {self.score} and over: {self.over}"
