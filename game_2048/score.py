import os
from typing import Union


class Score:
    def __init__(self) -> None:
        """Initializes the Score class with default scores."""
        self.current_score: int = 0
        self.best_score: int = self.load_best_score()

    def load_best_score(self) -> int:
        """Loads the best score from a file."""
        if os.path.exists("best_score.txt"):
            with open("best_score.txt", "r") as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 0
        return 0

    def save_best_score(self) -> None:
        """Saves the best score to a file."""
        with open("best_score.txt", "w") as f:
            f.write(str(self.best_score))

    def update_score(self, points: Union[int, "Score"]) -> None:
        """
        Updates the current score by adding the given points.

        Args:
            points (int or Score): The points to add to the current score.
        """
        if isinstance(points, Score):
            points = points.current_score
        self.current_score += points
        if self.current_score > self.best_score:
            self.best_score = self.current_score
            self.save_best_score()

    def reset_score(self) -> None:
        """Resets the current score to zero."""
        self.current_score = 0

    def get_current_score(self) -> int:
        """Returns the current score.

        Returns:
            int: The current score.
        """
        return self.current_score

    def get_best_score(self) -> int:
        """Returns the best score.

        Returns:
            int: The best score.
        """
        return self.best_score
