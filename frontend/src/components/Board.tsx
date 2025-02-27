import React, { useEffect, useState } from 'react';
import './Board.css';

interface BoardProps {
  board: number[][];
}

const Board: React.FC<BoardProps> = ({ board }) => {
  // Store the previous board state for animation reference.
  const [previousBoard, setPreviousBoard] = useState<number[][]>(board);

  // Initialize cellTransforms with identity (no offset) for each cell.
  const initialTransforms = board.map((row) =>
    row.map(() => 'translate(0, 0)')
  );
  const [cellTransforms, setCellTransforms] =
    useState<string[][]>(initialTransforms);

  // When the board changes, compute transform offsets for animation.
  useEffect(() => {
    // Compute new transforms based on differences between previousBoard and current board.
    const newTransforms = board.map((row, r) =>
      row.map((cell, c) => {
        if (cell === 0) return 'translate(0, 0)';
        // If the tile remains in its designated cell, no offset is needed.
        if (previousBoard[r] && previousBoard[r][c] === cell)
          return 'translate(0, 0)';
        // Search for the tile in the previous board using a top-down, left-right scan.
        for (let rPrev = 0; rPrev < previousBoard.length; rPrev++) {
          for (let cPrev = 0; cPrev < previousBoard[rPrev].length; cPrev++) {
            if (previousBoard[rPrev][cPrev] === cell) {
              // Calculate the horizontal offset in pixels.
              const diffX = (cPrev - c) * 110; // (previous column - current column) * (100px cell width + 10px gap)
              // Calculate the vertical offset in pixels.
              const diffY = (rPrev - r) * 110; // (previous row - current row) * (100px cell height + 10px gap)
              return `translate(${diffX}px, ${diffY}px)`;
            }
          }
        }
        return 'translate(0, 0)';
      })
    );
    // Set the computed offset transforms.
    setCellTransforms(newTransforms);

    // After a short delay, reset transforms to identity to animate the tile into their final positions.
    const timer = setTimeout(() => {
      const resetTransforms = board.map((row) =>
        row.map(() => 'translate(0, 0)')
      );
      setCellTransforms(resetTransforms);
    }, 60); // ms delay to allow the animation to start

    // Update the previousBoard after the animation completes.
    const boardTimer = setTimeout(() => {
      setPreviousBoard(board);
    }, 500); // ms delay to ensure the animation has completed

    return () => {
      clearTimeout(timer);
      clearTimeout(boardTimer);
    };
  }, [board, previousBoard]);

  return (
    <div className='board-container'>
      <div className='board'>
        {board.map((row, rowIndex) => (
          <div key={rowIndex} className='board-row'>
            {row.map((cell, cellIndex) => (
              <div
                key={cellIndex}
                className={`board-cell value-${cell}`}
                style={{ transform: cellTransforms[rowIndex][cellIndex] }}
              >
                {cell !== 0 ? cell : ''}
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Board;
