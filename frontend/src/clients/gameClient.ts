import { z } from 'zod';
import { API_BASE_URL } from '../settings';
import { getAuthHeaders, handleResponse } from './utils';

export const GameStateSchema = z.object({
  board: z.array(z.array(z.number())),
  score: z.number(),
  over: z.boolean(),
});

export const StartNewGameResponseSchema = z.object({
  game_state: GameStateSchema,
});

export const GameStateResponseSchema = z.object({
  game_state: GameStateSchema,
});

export const MakeMoveResponseSchema = z.object({
  status: z.enum(['success', 'failed']),
  message: z.string().optional(),
  game_state: GameStateSchema,
});

export const startNewGame = async () => {
  const response = await fetch(`${API_BASE_URL}/game/new/`, {
    method: 'POST',
    headers: {
      ...getAuthHeaders(),
    },
  });
  return handleResponse(response, StartNewGameResponseSchema);
};

export const fetchGameState = async () => {
  const response = await fetch(`${API_BASE_URL}/game/state/`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeaders(),
    },
  });
  return handleResponse(response, GameStateResponseSchema);
};

export const makeMove = async (move: string) => {
  const response = await fetch(`${API_BASE_URL}/game/move/?direction=${move}`, {
    method: 'POST',
    headers: {
      ...getAuthHeaders(),
    },
  });
  return handleResponse(response, MakeMoveResponseSchema);
};
