import React, { useState } from 'react';
import { useNavigate } from 'react-router';
import { login } from '../clients/authClient';
import { storeUserData } from '../utils/sessionUtils';
import './Login.css';

const Login: React.FC = () => {
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const data = await login(username, password);
      storeUserData(data);
      navigate('/game');
    } catch (error) {
      alert('Login failed. Please check your credentials and try again.');
    }
  };

  return (
    <div className='login-container'>
      <h2 className='login-title'>Login</h2>
      <form onSubmit={handleLogin} className='login-box'>
        <div>
          <label htmlFor='username'>Username:</label>
          <input
            type='text'
            id='username'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            className='login-input'
          />
        </div>
        <div>
          <label htmlFor='password'>Password:</label>
          <input
            type='password'
            id='password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            className='login-input'
          />
        </div>
        <button type='submit' className='login-button'>
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
