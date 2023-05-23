import React, { useState } from 'react';
import './login.css'
import axios from 'axios';

const LoginPage = () => {
  const [user, setUser] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async(e) => {
    e.preventDefault();
    // Handle login logic here
    console.log("username",user,"password",password)
    try {
      const response = await axios.post('http://127.0.0.1:8000/signin/', {
        headers: {
          'Access-Control-Allow-Origin': '*',
          "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
          'Content-Type': 'application/json',
          Accept: 'application/json',
      },  
        // Request body data
        username: user,
        password:password ,
      });
  
      console.log('Response:', response);
    } catch (error) {
      console.error('Error:', error);
    }
  };
  
    
  

  return (
    <div className="form-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <label>
          Username:
          <input type="text" value={user} onChange={(e) => setUser(e.target.value)} />
        </label>
        <br />
        <label>
          Password:
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage