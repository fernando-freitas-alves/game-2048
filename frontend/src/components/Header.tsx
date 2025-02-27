import React from 'react';
import { useNavigate } from 'react-router';
import { logout } from '../clients/loginClient';
import './Header.css';

const Header: React.FC = () => {
  const navigate = useNavigate();
  const user = JSON.parse(sessionStorage.getItem('user') || '{}');

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
