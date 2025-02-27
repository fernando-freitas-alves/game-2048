import React from 'react';
import { useNavigate } from 'react-router';
import { logout } from '../clients/authClient';
import './Header.css';

const Header: React.FC = () => {
  const navigate = useNavigate();
  const userString = sessionStorage.getItem('user');
  const user = userString ? JSON.parse(userString) : {};

  const handleLogout = async () => {
    await logout();
    sessionStorage.clear();
    navigate('/');
  };

  return (
    <div className='header'>
      <span>{user.username}</span>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Header;
