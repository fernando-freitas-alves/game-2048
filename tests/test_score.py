import unittest
from unittest.mock import patch
from game_2048.score import Score


class TestScore(unittest.TestCase):
    @patch("os.path.exists")
    @patch("os.rename")
    @patch("os.remove")
    def setUp(self, mock_remove, mock_rename, mock_exists):
        # Mock os.path.exists to simulate the absence of best_score.txt
        mock_exists.return_value = False
        self.score = Score()

    @patch("os.path.exists")
    @patch("os.rename")
    @patch("os.remove")
    def tearDown(self, mock_remove, mock_rename, mock_exists):
        # Ensure that os.remove and os.rename are not called during teardown
        mock_remove.assert_not_called()
        mock_rename.assert_not_called()

    def test_initial_scores(self):
        self.assertEqual(self.score.get_current_score(), 0)
        self.assertEqual(self.score.get_best_score(), 0)

    def test_update_score(self):
        self.score.update_score(10)
        self.assertEqual(self.score.get_current_score(), 10)
        self.assertEqual(self.score.get_best_score(), 10)

        self.score.update_score(20)
        self.assertEqual(self.score.get_current_score(), 30)
        self.assertEqual(self.score.get_best_score(), 30)

    def test_best_score_persistence(self):
        self.score.update_score(50)
        self.assertEqual(self.score.get_best_score(), 50)

        # Create a new Score instance to check persistence
        new_score = Score()
        self.assertEqual(new_score.get_best_score(), 50)

    def test_reset_score(self):
        self.score.update_score(100)
        self.score.reset_score()
        self.assertEqual(self.score.get_current_score(), 0)
        self.assertEqual(self.score.get_best_score(), 100)


if __name__ == "__main__":
    unittest.main()
