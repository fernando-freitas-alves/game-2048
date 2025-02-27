import React, { useState } from 'react';
import { useNavigate } from 'react-router';
import { signup } from '../clients/authClient';
import { storeUserData } from '../utils/sessionUtils';
import './SignUp.css';

const SignUp: React.FC = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');

  const handleSignUp = async (event: React.FormEvent) => {
    event.preventDefault();
    try {
      const data = await signup(username, password, email);
      console.log('data', data);
      storeUserData(data);
      navigate('/game');
    } catch (error) {
      alert('Sign up failed. Please check your details and try again.');
    }
  };

  return (
    <div className='signup-container'>
      <h2 className='signup-title'>Sign Up</h2>
      <form onSubmit={handleSignUp} className='signup-box'>
        <div>
          <label htmlFor='username'>Username:</label>
          <input
            type='text'
            id='username'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            className='signup-input'
          />
        </div>
        <div>
          <label htmlFor='email'>Email:</label>
          <input
            type='email'
            id='email'
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            className='signup-input'
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
            className='signup-input'
          />
        </div>
        <button type='submit' className='signup-button'>
          Sign Up
        </button>
      </form>
    </div>
  );
};

export default SignUp;
