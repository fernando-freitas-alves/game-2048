import React from 'react';
import { RouterProvider, createBrowserRouter } from 'react-router';
import Home from './components/Home';
import Login from './components/Login';
import Game from './screens/Game';
import './App.css';

const App: React.FC = () => {
  const router = createBrowserRouter([
    {
      path: '/',
      element: <Home />,
    },
    {
      path: '/login',
      element: <Login />,
    },
    {
      path: '/game',
      element: <Game />,
    },
  ]);

  return <RouterProvider router={router} />;
};

export default App;
