import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import CssBaseline from '@mui/material/CssBaseline';
import Navbar from './components/layout/Navbar';
import Home from './pages/Home';
import Jobs from './pages/Jobs';

function App() {
  return (
    <Router>
      <CssBaseline />
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/jobs" element={<Jobs />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
