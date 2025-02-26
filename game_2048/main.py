from .game import Game
from .score import Score
from .ui import UI


class Main:
    def __init__(self) -> None:
        """Initializes the Main class with Game, UI, and Score instances."""
        self.game = Game()
        self.score = Score()
        self.ui = UI(self.game, self.score)

    def main(self) -> None:
        """Runs the main game loop."""
        self.ui.initialize_pygame()
        while True:
            self.ui.handle_input()
            self.ui.update_display()


if __name__ == "__main__":
    main_instance = Main()
    main_instance.main()
