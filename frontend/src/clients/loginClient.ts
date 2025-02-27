import { API_BASE_URL } from './contants';
import { getAuthHeaders } from './utils';

export const login = async (
  username: string,
  password: string
): Promise<any> => {
  try {
    const response = await fetch(`${API_BASE_URL}/auth/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),
    });

    return response;
  } catch (error) {
    console.error('Error during login:', error);
    return false;
  }
};

export const logout = async (): Promise<void> => {
  try {
    await fetch(`${API_BASE_URL}/auth/logout/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...getAuthHeaders(),
      },
    });
  } catch (error) {
    console.error('Error during logout:', error);
  }
};
