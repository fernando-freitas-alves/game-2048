export const getAuthHeaders = () => ({
  Authorization: `Token ${sessionStorage.getItem('token')}`,
});
