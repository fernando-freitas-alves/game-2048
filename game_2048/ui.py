import pygame

from .game import Game
from .score import Score


class UI:
    def __init__(self, game: Game, score: Score) -> None:
        """Initializes the UI class with a game and score instance.

        Args:
            game (Game): The game instance to interact with.
            score (Score): The score instance to manage scores.
        """
        self.game = game
        self.score = score
        self.screen: pygame.surface.Surface
        self.font: pygame.font.Font
        self.tile_size = 100
        self.margin = 10
        self.window_size = (self.tile_size * 4 + self.margin * 5, self.tile_size * 4 + self.margin * 6 + 100)
        self.background_color = (187, 173, 160)
        self.tile_colors = {
            0: (205, 193, 180),
            2: (238, 228, 218),
            4: (237, 224, 200),
            8: (242, 177, 121),
            16: (245, 149, 99),
            32: (246, 124, 95),
            64: (246, 94, 59),
            128: (237, 207, 114),
            256: (237, 204, 97),
            512: (237, 200, 80),
            1024: (237, 197, 63),
            2048: (237, 194, 46),
        }
        self.initialize_pygame()

    def render(self) -> None:
        """Renders the game board and score on the screen."""
        self.screen.fill(self.background_color)
        for i in range(4):
            for j in range(4):
                self._draw_tile(i, j)
        self._draw_score()
        pygame.display.flip()

    def handle_input(self) -> None:
        """Handles user input for game control."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self._process_move("up")
                elif event.key == pygame.K_DOWN:
                    self._process_move("down")
                elif event.key == pygame.K_LEFT:
                    self._process_move("left")
                elif event.key == pygame.K_RIGHT:
                    self._process_move("right")

    def update_display(self) -> None:
        """Updates the display after handling input and game logic."""
        self.render()

    def _draw_tile(self, row: int, col: int) -> None:
        """Draws a single tile on the board.

        Args:
            row (int): The row index of the tile.
            col (int): The column index of the tile.
        """
        value = self.game.board[row][col]
        color = self.tile_colors.get(value, (60, 58, 50))
        x = self.margin + col * (self.tile_size + self.margin)
        y = self.margin + row * (self.tile_size + self.margin) + 100
        pygame.draw.rect(self.screen, color, (x, y, self.tile_size, self.tile_size))
        if value != 0:
            text_surface = self.font.render(str(value), True, (119, 110, 101))
            text_rect = text_surface.get_rect(center=(x + self.tile_size / 2, y + self.tile_size / 2))
            self.screen.blit(text_surface, text_rect)

    def _draw_score(self) -> None:
        """Draws the current and best scores on the screen."""
        current_score_text = f"Score: {self.score.get_current_score()}"
        best_score_text = f"Best: {self.score.get_best_score()}"
        current_score_surface = self.font.render(current_score_text, True, (119, 110, 101))
        best_score_surface = self.font.render(best_score_text, True, (119, 110, 101))
        self.screen.blit(current_score_surface, (self.margin, self.margin))
        self.screen.blit(best_score_surface, (self.margin, self.margin + 40))

    def _process_move(self, direction: str) -> None:
        """Processes a move in the given direction and updates the score.

        Args:
            direction (str): The direction to move the tiles.
        """
        if self.game.move(direction):
            self.score.update_score(self.game.score)
            if self.game.is_game_over():
                self._game_over()

    def _game_over(self) -> None:
        """Handles the game over state."""
        banner_height = 60
        banner_color = (0, 0, 0, 128)  # Semi-transparent black
        banner_rect = pygame.Surface((self.window_size[0], banner_height), pygame.SRCALPHA)
        banner_rect.fill(banner_color)
        self.screen.blit(banner_rect, (0, self.window_size[1] // 2 - banner_height // 2))

        game_over_surface = self.font.render("Game Over!", True, (255, 255, 255))
        text_rect = game_over_surface.get_rect(center=(self.window_size[0] // 2, self.window_size[1] // 2))
        self.screen.blit(game_over_surface, text_rect)
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds
        self.game.reset()
        self.score.reset_score()

    def initialize_pygame(self) -> None:
        """Initializes the Pygame library and sets up the display."""
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("2048 Game")
        self.font = pygame.font.Font(None, 36)
