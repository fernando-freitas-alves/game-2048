import unittest
from unittest.mock import Mock, patch

from game.engine.game_engine import GameEngine


class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up a new GameEngine instance for each test."""
        self.game = GameEngine()

    def test_initial_board(self):
        """Test that the board is initialized correctly with two tiles."""
        non_zero_tiles = sum(cell != 0 for row in self.game.board for cell in row)
        self.assertEqual(
            non_zero_tiles,
            2,
            "Initial board should have exactly two tiles.",
        )

    @patch("game.engine.game_engine.GameEngine.add_random_tile")
    def test_move_up(self, mock_add_random_tile: Mock):
        """Test that moving up merges tiles correctly."""
        # Set up a specific board state
        self.game.board = [
            [2, 0, 0, 2],
            [0, 0, 0, 0],
            [2, 0, 0, 2],
            [0, 0, 0, 0],
        ]
        moved = self.game.move("up")
        expected_board = [
            [4, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertTrue(moved, "Move up should result in a change.")
        self.assertEqual(
            self.game.board,
            expected_board,
            "Tiles should merge correctly when moving up.",
        )

    @patch("game.engine.game_engine.GameEngine.add_random_tile")
    def test_move_down(self, mock_add_random_tile: Mock):
        """Test that moving down merges tiles correctly."""
        # Set up a specific board state
        self.game.board = [
            [2, 0, 0, 2],
            [0, 0, 0, 0],
            [2, 0, 0, 2],
            [0, 0, 0, 0],
        ]
        moved = self.game.move("down")
        expected_board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 4],
        ]
        self.assertTrue(moved, "Move down should result in a change.")
        self.assertEqual(
            self.game.board,
            expected_board,
            "Tiles should merge correctly when moving down.",
        )

    @patch("game.engine.game_engine.GameEngine.add_random_tile")
    def test_move_left(self, mock_add_random_tile: Mock):
        """Test that moving left merges tiles correctly."""
        # Set up a specific board state
        self.game.board = [
            [2, 2, 0, 0],
            [4, 0, 4, 0],
            [0, 0, 0, 0],
            [8, 8, 8, 8],
        ]
        moved = self.game.move("left")
        expected_board = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [16, 16, 0, 0],
        ]
        self.assertTrue(moved, "Move left should result in a change.")
        self.assertEqual(
            self.game.board,
            expected_board,
            "Tiles should merge correctly when moving left.",
        )

    @patch("game.engine.game_engine.GameEngine.add_random_tile")
    def test_move_right(self, mock_add_random_tile: Mock):
        """Test that moving right merges tiles correctly."""
        # Set up a specific board state
        self.game.board = [
            [0, 0, 2, 2],
            [0, 4, 0, 4],
            [0, 0, 0, 0],
            [8, 8, 8, 8],
        ]
        moved = self.game.move("right")
        expected_board = [
            [0, 0, 0, 4],
            [0, 0, 0, 8],
            [0, 0, 0, 0],
            [0, 0, 16, 16],
        ]
        self.assertTrue(moved, "Move right should result in a change.")
        self.assertEqual(
            self.game.board,
            expected_board,
            "Tiles should merge correctly when moving right.",
        )

    @patch("random.choice")
    def test_add_random_tile(self, mock_random_choice: Mock):
        """Test that a new tile is added after a successful move."""
        # Mock random.choice to control where and what tile is added
        # First call: choose position (1, 1)
        # Second call: choose tile value 2
        mock_random_choice.side_effect = [(1, 1), 2]

        # Set up a specific board state that will change after a move
        self.game.board = [
            [2, 0, 0, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        # Test that a new tile is added after a move
        initial_tiles = sum(cell != 0 for row in self.game.board for cell in row)
        moved = self.game.move("left")  # This move should merge and add a tile
        if moved:
            new_tiles = sum(cell != 0 for row in self.game.board for cell in row)
            self.assertEqual(
                new_tiles,
                initial_tiles,
                (
                    "A new tile should be added after a successful move "
                    "but the overall num of tiles shouldn't change since there was a merge in the previous move."
                ),
            )
            # Verify that the new tile was added at position (0,1) with value 2
            self.assertEqual(
                self.game.board[1][1],
                2,
                "A new tile with value 2 should be added at position (1, 1).",
            )
        else:
            self.fail("Move did not result in a change, cannot test tile addition.")

    def test_reset_game(self):
        """Test resetting the game."""
        self.game.reset()
        non_zero_tiles = sum(cell != 0 for row in self.game.board for cell in row)
        self.assertEqual(
            non_zero_tiles,
            2,
            "After reset, the board should have exactly two tiles.",
        )
