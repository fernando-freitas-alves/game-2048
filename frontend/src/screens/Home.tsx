import React from 'react';
import { useNavigate } from 'react-router';
import './Home.css';

const gameboardImage = process.env.PUBLIC_URL + '/2048-gameboard-modern.png';

const Home: React.FC = () => {
  const navigate = useNavigate();

  return (
    <div className='home-container'>
      <img
        src={gameboardImage}
        alt='2048 Gameboard'
        className='gameboard-image'
      />
      <div className='right-content'>
        <h1>Welcome to the Game!</h1>
        <button className='login-button' onClick={() => navigate('/login')}>
          Login
        </button>
        <button className='signup-button' onClick={() => navigate('/signup')}>
          Sign Up
        </button>
      </div>
    </div>
  );
};

export default Home;
