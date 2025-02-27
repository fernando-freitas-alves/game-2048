import React from 'react';
import { RouterProvider, createBrowserRouter } from 'react-router';
import './App.css';
import Game from './screens/Game';
import Home from './screens/Home';
import Login from './screens/Login';
import SignUp from './screens/SignUp';

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
      path: '/signup',
      element: <SignUp />,
    },
    {
      path: '/game',
      element: <Game />,
    },
  ]);

  return <RouterProvider router={router} />;
};

export default App;
