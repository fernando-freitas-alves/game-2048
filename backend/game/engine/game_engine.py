import random
from typing import List


class GameEngine:
    board: List[List[int]]
    score: int

    def __init__(self) -> None:
        """Initializes the Game with a board and score."""
        self.reset()

    def move(self, direction: str) -> bool:
        """Moves the tiles in the specified direction.

        Args:
            direction (str): The direction to move the tiles ('up', 'down', 'left', 'right').

        Returns:
            bool: True if the board changed, False otherwise.
        """
        if direction not in ["up", "down", "left", "right"]:
            return False

        original_board = [row[:] for row in self.board]
        self._move(direction)

        if self.board != original_board:
            self.add_random_tile()
            return True
        return False

    def _move(self, direction: str) -> None:
        """Handles the logic for moving tiles in the specified direction.

        Args:
            direction (str): The direction to move the tiles ('up', 'down', 'left', 'right').
        """
        for i in range(4):  # Iterate over each row/column
            if direction in ["up", "down"]:
                # Extract the column as a line
                line = [self.board[j][i] for j in range(4)]
            else:
                # Use the row as a line
                line = self.board[i]

            if direction in ["down", "right"]:
                # Reverse the line for 'down' or 'right' to handle merging
                line = self._compress(line, reverse=True)
                line = self._merge(line, reverse=True)
                line = self._compress(line, reverse=True)
            else:
                # Handle 'up' or 'left' without reversing
                line = self._compress(line)
                line = self._merge(line)
                line = self._compress(line)

            for j in range(4):  # Place the processed line back into the board
                if direction in ["up", "down"]:
                    self.board[j][i] = line[j]
                else:
                    self.board[i][j] = line[j]

    def add_random_tile(self) -> None:
        """Adds a random tile (2 or 4) to an empty spot on the board."""
        empty_tiles = self._get_empty_tiles()
        if not empty_tiles:
            return
        i, j = random.choice(empty_tiles)  # nosec
        self.board[i][j] = random.choice([2, 4])  # nosec

    def _get_empty_tiles(self) -> List[tuple]:
        """Gets a list of empty tile positions on the board.

        Returns:
            List[tuple]: A list of tuples representing the positions of empty tiles.
        """
        return [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]

    def is_game_over(self) -> bool:
        """Checks if there are no valid moves left.

        Returns:
            bool: True if no valid moves are left, False otherwise.
        """
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
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()

    def _compress(self, line: List[int], reverse: bool = False) -> List[int]:
        """Compresses the tiles in a line by sliding them towards the specified direction.

        Args:
            line (List[int]): The line of tiles to compress.
            reverse (bool, optional): Whether to reverse the direction. Defaults to False.

        Returns:
            List[int]: The compressed line of tiles.
        """
        tiles = [tile for tile in line if tile != 0]
        if reverse:
            tiles.reverse()
        tiles += [0] * (4 - len(tiles))
        if reverse:
            tiles.reverse()
        return tiles

    def _merge(self, line: List[int], reverse: bool = False) -> List[int]:
        """Merges the tiles in a line after compression.

        Args:
            line (List[int]): The line of tiles to merge.
            reverse (bool, optional): Whether to reverse the direction. Defaults to False.

        Returns:
            List[int]: The merged line of tiles.
        """
        range_start, range_end, step = (0, 3, 1) if not reverse else (3, 0, -1)
        for i in range(range_start, range_end, step):
            if line[i] == line[i + step] and line[i] != 0:
                line[i] *= 2
                self.score += line[i]
                line[i + step] = 0
        return line
