import unittest
from unittest.mock import mock_open, patch

from game_2048.game import Game
from game_2048.score import Score


class TestGame(unittest.TestCase):
    @patch("game_2048.score.os.path.exists")
    @patch("game_2048.score.os.rename")
    @patch("game_2048.score.os.remove")
    @patch("builtins.open", new_callable=mock_open, read_data="0")
    def setUp(self, mock_file, mock_remove, mock_rename, mock_exists):
        """Set up a new Game and Score instance for each test."""
        # Mock os.path.exists to simulate the absence of best_score.txt
        mock_exists.return_value = False
        self.game = Game()
        self.score = Score()

    @patch("game_2048.score.os.path.exists")
    @patch("game_2048.score.os.rename")
    @patch("game_2048.score.os.remove")
    @patch("builtins.open", new_callable=mock_open, read_data="0")
    def tearDown(self, mock_file, mock_remove, mock_rename, mock_exists):
        """Tear down after each test."""
        # Ensure that os.remove and os.rename are not called during teardown
        mock_remove.assert_not_called()
        mock_rename.assert_not_called()

    def test_initial_board(self):
        """Test that the board is initialized correctly with two tiles."""
        non_zero_tiles = sum(cell != 0 for row in self.game.board for cell in row)
        self.assertEqual(
            non_zero_tiles,
            2,
            "Initial board should have exactly two tiles.",
        )

    @patch("game_2048.game.Game.add_random_tile")
    def test_move_up(self, mock_add_random_tile):
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

    @patch("game_2048.game.Game.add_random_tile")
    def test_move_down(self, mock_add_random_tile):
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

    @patch("game_2048.game.Game.add_random_tile")
    def test_move_left(self, mock_add_random_tile):
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

    @patch("game_2048.game.Game.add_random_tile")
    def test_move_right(self, mock_add_random_tile):
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
    def test_add_random_tile(self, mock_random_choice):
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

    @patch("game_2048.score.os.path.exists")
    @patch("game_2048.score.os.rename")
    @patch("game_2048.score.os.remove")
    @patch("builtins.open", new_callable=mock_open, read_data="100")
    def test_reset_game(self, mock_file, mock_remove, mock_rename, mock_exists):
        """Test resetting the game."""
        # Test resetting the game
        self.score.update_score(100)
        self.game.reset()
        self.score.reset_score()
        self.assertEqual(
            self.score.get_current_score(),
            0,
            "Current score should be reset to 0.",
        )
        non_zero_tiles = sum(cell != 0 for row in self.game.board for cell in row)
        self.assertEqual(
            non_zero_tiles,
            2,
            "After reset, the board should have exactly two tiles.",
        )


if __name__ == "__main__":
    unittest.main()
    unittest.main()
