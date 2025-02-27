import { z } from 'zod';
import { AuthResponseSchema } from '../clients/authClient';

export type AuthResponse = z.infer<typeof AuthResponseSchema>;

export const storeUserData = (data: AuthResponse) => {
  if (data.user && data.token) {
    sessionStorage.setItem('user', JSON.stringify(data.user));
    sessionStorage.setItem('token', data.token);
  } else {
    throw new Error('Invalid response data');
  }
};
