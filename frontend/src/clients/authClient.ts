import { z } from 'zod';
import { API_BASE_URL } from '../settings';
import { getAuthHeaders, handleResponse } from './utils';

export const AuthResponseSchema = z.object({
  user: z.object({
    username: z.string(),
    email: z.string(),
  }),
  token: z.string(),
});

export const signup = async (
  username: string,
  password: string,
  email: string
) => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/signup/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password, email }),
    });
    return handleResponse(response, AuthResponseSchema);
  } catch (error) {
    throw new Error('Error during sign up');
  }
};

export const login = async (username: string, password: string) => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });
    return handleResponse(response, AuthResponseSchema);
  } catch (error) {
    throw new Error('Error during login');
  }
};

export const logout = async () => {
  try {
    await fetch(`${API_BASE_URL}/auth/logout/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...getAuthHeaders(),
      },
    });
  } catch (error) {}
};
