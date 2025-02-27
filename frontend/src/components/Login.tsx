import React, { useState } from 'react';
import { login } from '../clients/loginClient';
import { useNavigate } from 'react-router';
import './Login.css';

const Login: React.FC = () => {
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async (event: React.FormEvent) => {
    event.preventDefault();
    const response = await login(username, password);
    if (response.ok) {
      const data = await response.json();
      // Store user details and token in session storage
      sessionStorage.setItem('user', JSON.stringify(data.user));
      sessionStorage.setItem('token', data.token);
      // Redirect to the game screen on successful login
      navigate('/game');
    } else {
      // Handle login failure
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
