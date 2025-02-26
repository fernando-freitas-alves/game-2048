# 2048 Game

## Overview

This is a Python implementation of the classic 2048 game using Pygame. The game features:

- **Interactive user interface**
- **Score tracking with best score preservation**
- **Game over detection and reset functionality**

## Installation

### Prerequisites

- **Python 3.x**
- **Pygame library**

### Setup

Use the `Makefile` to set up the project environment and install dependencies:

```bash
make setup
```

This will:

1. Create a Python virtual environment named `venv`.
2. Activate the virtual environment.
3. Install the required dependencies from `requirements.txt`.

## How to Run

Use the `Makefile` to run the game:

```bash
make run
```

This will:

1. Activate the Python virtual environment.
2. Start the game by running `game_2048/main.py`.

## How to Test

Use the `Makefile` to run unit tests:

```bash
make test
```

This will:

1. Activate the Python virtual environment.
2. Execute all unit tests located in the `tests/` directory to ensure that the game's core functionalities work as expected.

## Makefile

The `Makefile` provides convenient targets to manage the project:

- **setup**: Create a virtual environment and install dependencies.

  ```bash
  make setup
  ```

- **run**: Activate the virtual environment and run the game.

  ```bash
  make run
  ```

- **test**: Activate the virtual environment and run unit tests.

  ```bash
  make test
  ```

- **help**: Display available Makefile targets.

  ```bash
  make help
  ```

## Project Structure

- `game_2048/`: Contains the main game code.
  - `main.py`: Entry point of the application.
  - `game.py`: Handles game logic.
  - `score.py`: Manages scoring.
  - `ui.py`: Manages the user interface.
- `resources/`: Contains additional resources and documentation.
- `tests/`: Contains unit tests for the game.
  - `test_score.py`: Tests for the `Score` class.
  - `test_game.py`: Tests for the `Game` class.
- `docs/`: Documentation related files.
- `Makefile`: Automation scripts for setup, running, and testing the project.
- `README.md`: Project documentation and instructions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
