import React, { useCallback, useEffect, useState } from 'react';
import { fetchGameState, makeMove, startNewGame } from '../clients/gameClient';
import Board from '../components/Board';
import Header from '../components/Header';
import Score from '../components/Score';
import { DEBOUNCE_DELAY_MILLISECONDS } from '../settings';
import { debounce } from '../utils/debounce';
import './Game.css';

type Move = 'up' | 'down' | 'left' | 'right';

const Game: React.FC = () => {
  const [gameState, setGameState] = useState<{
    score?: number;
    board: number[][];
    over: boolean;
  }>({
    score: undefined,
    board: [
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
    ],
    over: false,
  });

  useEffect(() => {
    fetchGameState()
      .then((data) => setGameState(data.game_state))
      .catch((error) => console.error('Failed to fetch game state', error));
  }, []);

  const handleMove = useCallback((move: Move) => {
    makeMove(move)
      .then((data) => {
        setGameState(data.game_state);
      })
      .catch((error) => console.error('Failed to make move', error));
  }, []);

  const handleStartNewGame = () => {
    startNewGame()
      .then((data) => setGameState(data.game_state))
      .catch((error) => console.error('Failed to start new game', error));
  };

  useEffect(() => {
    const handleKeyDown = debounce((event: KeyboardEvent) => {
      if (gameState.over) return;

      switch (event.key) {
        case 'ArrowUp':
          event.preventDefault();
          handleMove('up');
          break;
        case 'ArrowDown':
          event.preventDefault();
          handleMove('down');
          break;
        case 'ArrowLeft':
          event.preventDefault();
          handleMove('left');
          break;
        case 'ArrowRight':
          event.preventDefault();
          handleMove('right');
          break;
        default:
          break;
      }
    }, DEBOUNCE_DELAY_MILLISECONDS);

    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [handleMove, gameState.over]);

  return (
    <div>
      <Header />
      <h1 className='game-title'>2048 Game</h1>
      <Score score={gameState.score} />
      <Board board={gameState.board} />
      {gameState.over && (
        <div className='over-game-banner'>
          <p>Game Over</p>
          <button
            className='start-new-game-button'
            onClick={handleStartNewGame}
          >
            Start New Game
          </button>
        </div>
      )}
    </div>
  );
};

export default Game;
