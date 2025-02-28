import { z } from 'zod';

export const getAuthHeaders = () => ({
  Authorization: `Token ${sessionStorage.getItem('token')}`,
});

export const handleResponse = async <T>(
  response: Response,
  schema: z.ZodSchema<T>
): Promise<T> => {
  if (!response.ok) {
    throw new Error('Failed to fetch data');
  }
  const json = await response.json();
  return schema.parse(json);
};
