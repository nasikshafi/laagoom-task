import React, { useState } from 'react';
import './login.css'
import axios from 'axios';
const RegisterPage = () => {
    const [email, setEmail] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
  
    const handleRegister = (e) => {
      e.preventDefault();
      // Handle registration logic here
      console.log('Registering...');
    };
  
    return (
      <div className="form-container">
        <h2>Register</h2>
        <form onSubmit={handleRegister}>
        <label>
            Username:
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} />
          </label>
          <br />
          <label>
            Email:
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
          </label>
          <br />
          <label>
            Password:
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </label>
          <br />
          <button type="submit">Register</button>
        </form>
      </div>
    );
  };
  

export default RegisterPage