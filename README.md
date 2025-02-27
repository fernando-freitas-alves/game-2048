# 2048 Game

<!-- markdownlint-disable MD033 -->
<p align="center">
  <img width="582" alt="image" src="https://github.com/user-attachments/assets/81570416-daa1-49d9-ae68-555f4ebc0eaf" />
</p>

## Overview

This project is a full-stack implementation of the classic 2048 game using Django for the backend and React for the
frontend. The game features:

- **Interactive user interface**
- **Score tracking with best score preservation**
- **Game over detection and reset functionality**
- **Server-side game storage with login for accessing previous games**

## Installation

### Prerequisites

- **Python 3.12**
- **Node.js 16+ and npm**

### Setup

Use the `Makefile` to set up the project environment and install dependencies:

```bash
make setup
```

This will:

1. Create a Python virtual environment named `.venv` in the `backend` folder and install the required dependencies from
   `requirements-dev.txt`.
2. Install the required Node.js packages in the `frontend` folder.

## How to Run

### Backend

Use the `Makefile` to run the game server:

```bash
make run-backend
```

### Frontend

Use the `Makefile` to run the game client:

```bash
make run-frontend
```

## How to Test

### Backend Tests

Use the `Makefile` to run unit tests:

```bash
make test
```

## Additional Makefile Commands

### Create Superuser

Use the `Makefile` to create a superuser for the backend:

```bash
make create-superuser
```

### Migrations

Use the `Makefile` to make and apply database migrations:

```bash
make migrations
```

### Lint

Use the `Makefile` to run all linters via pre-commit:

```bash
make lint
```

### Help

Use the `Makefile` to show the help message with available targets:

```bash
make help
```

## Project Structure

- `backend/`: Contains the Django backend code.
  - `authentication/`: Handles user authentication.
  - `game/`: Contains game logic and models.
  - `main/`: Main application settings and URLs.
- `frontend/`: Contains the React frontend code.
  - `src/`: Source code for React components and utilities.
- `tests/`: Contains unit tests for the backend.
- `Makefile`: Automation scripts for setup, running, and testing the backend.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
