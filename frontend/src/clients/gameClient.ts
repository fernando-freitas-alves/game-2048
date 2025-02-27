import { API_BASE_URL } from './contants';
import { getAuthHeaders } from './utils';

export interface GameState {
  board: number[][];
  score: number;
  over: boolean;
}

export interface FetchGameStateResponse {
  game_state: GameState;
}

export interface MakeMoveResponse {
  status: 'success' | 'failed';
  message?: string;
  game_state: GameState;
}

export interface StartNewGameResponse {
  game_state: GameState;
}

const handleResponse = async (response: Response): Promise<any> => {
  if (!response.ok) {
    throw new Error('Failed to fetch data');
  }
  return response.json();
};

export const fetchGameState = async (): Promise<FetchGameStateResponse> => {
  const response = await fetch(`${API_BASE_URL}/game/state/`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      ...getAuthHeaders(),
    },
  });
  return handleResponse(response);
};

export const makeMove = async (move: string): Promise<MakeMoveResponse> => {
  const response = await fetch(`${API_BASE_URL}/game/move/?direction=${move}`, {
    method: 'POST',
    headers: {
      ...getAuthHeaders(),
    },
  });
  return handleResponse(response);
};

export const startNewGame = async (): Promise<StartNewGameResponse> => {
  const response = await fetch(`${API_BASE_URL}/game/start/`, {
    method: 'POST',
    headers: {
      ...getAuthHeaders(),
    },
  });
  return handleResponse(response);
};
