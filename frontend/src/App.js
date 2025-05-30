import React from 'react';
import { Routes, Route } from 'react-router-dom';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Job Search Platform</h1>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<div>Home Page</div>} />
          <Route path="/jobs" element={<div>Jobs Page</div>} />
          <Route path="/login" element={<div>Login Page</div>} />
          <Route path="/register" element={<div>Register Page</div>} />
        </Routes>
      </main>
    </div>
  );
}

export default App; 