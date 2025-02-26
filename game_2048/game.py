import random
from typing import List

from .score import Score


class Game:
    def __init__(self) -> None:
        """Initializes the Game with a board and score."""
        self.board: List[List[int]] = [[0] * 4 for _ in range(4)]
        self.score = Score()
        self.add_random_tile()
        self.add_random_tile()

    def move(self, direction: str) -> bool:
        """Moves the tiles in the specified direction."""
        if direction not in ["up", "down", "left", "right"]:
            return False

        original_board = [row[:] for row in self.board]
        if direction == "up":
            self._move_up()
        elif direction == "down":
            self._move_down()
        elif direction == "left":
            self._move_left()
        elif direction == "right":
            self._move_right()

        if self.board != original_board:
            self.add_random_tile()
            return True
        return False

    def add_random_tile(self) -> None:
        """Adds a random tile (2 or 4) to an empty spot on the board."""
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if not empty_tiles:
            return
        i, j = random.choice(empty_tiles)  # nosec
        self.board[i][j] = random.choice([2, 4])  # nosec

    def is_game_over(self) -> bool:
        """Checks if there are no valid moves left."""
        if any(0 in row for row in self.board):
            return False
        for i in range(4):
            for j in range(4):
                if (i < 3 and self.board[i][j] == self.board[i + 1][j]) or (
                    j < 3 and self.board[i][j] == self.board[i][j + 1]
                ):
                    return False
        return True

    def reset(self) -> None:
        """Resets the game board and score."""
        self.board = [[0] * 4 for _ in range(4)]
        self.score.reset_score()
        self.add_random_tile()
        self.add_random_tile()

    def _move_up(self) -> None:
        """Handles the logic for moving tiles up."""
        for j in range(4):
            self._compress_column(j)
            self._merge_column(j)
            self._compress_column(j)

    def _move_down(self) -> None:
        """Handles the logic for moving tiles down."""
        for j in range(4):
            self._compress_column(j, reverse=True)
            self._merge_column(j, reverse=True)
            self._compress_column(j, reverse=True)

    def _move_left(self) -> None:
        """Handles the logic for moving tiles left."""
        for i in range(4):
            self._compress_row(i)
            self._merge_row(i)
            self._compress_row(i)

    def _move_right(self) -> None:
        """Handles the logic for moving tiles right."""
        for i in range(4):
            self._compress_row(i, reverse=True)
            self._merge_row(i, reverse=True)
            self._compress_row(i, reverse=True)

    def _compress_row(self, row: int, reverse: bool = False) -> None:
        """Compresses the tiles in a row by sliding them towards the specified direction."""
        tiles = [self.board[row][j] for j in range(4) if self.board[row][j] != 0]
        if reverse:
            tiles.reverse()
        tiles += [0] * (4 - len(tiles))
        if reverse:
            tiles.reverse()
        self.board[row] = tiles

    def _merge_row(self, row: int, reverse: bool = False) -> None:
        """Merges the tiles in a row after compression."""
        range_start, range_end, step = (0, 3, 1) if not reverse else (3, 0, -1)
        for j in range(range_start, range_end, step):
            if self.board[row][j] == self.board[row][j + step] and self.board[row][j] != 0:
                self.board[row][j] *= 2
                self.score.update_score(self.board[row][j])
                self.board[row][j + step] = 0

    def _compress_column(self, col: int, reverse: bool = False) -> None:
        """Compresses the tiles in a column by sliding them towards the specified direction."""
        tiles = [self.board[i][col] for i in range(4) if self.board[i][col] != 0]
        if reverse:
            tiles.reverse()
        tiles += [0] * (4 - len(tiles))
        if reverse:
            tiles.reverse()
        for i in range(4):
            self.board[i][col] = tiles[i]

    def _merge_column(self, col: int, reverse: bool = False) -> None:
        """Merges the tiles in a column after compression."""
        range_start, range_end, step = (0, 3, 1) if not reverse else (3, 0, -1)
        for i in range(range_start, range_end, step):
            if self.board[i][col] == self.board[i + step][col] and self.board[i][col] != 0:
                self.board[i][col] *= 2
                self.score.update_score(self.board[i][col])
                self.board[i + step][col] = 0


if __name__ == "__main__":
    game = Game()
    # Additional game loop or interactions can be added here
