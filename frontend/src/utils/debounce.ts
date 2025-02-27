/**
 * Debounce function to limit the rate at which a function can fire.
 * @param func - The function to debounce.
 * @param wait - The number of milliseconds to delay.
 * @returns A debounced version of the function.
 */
export const debounce = (func: (...args: any[]) => void, wait: number) => {
  let timeout: ReturnType<typeof setTimeout> | undefined;
  return (...args: any[]) => {
    if (!timeout) {
      func(...args);
    }
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      timeout = undefined;
    }, wait);
  };
};
