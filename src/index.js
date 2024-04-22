import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './header';
import Footer from './footer';
import Register from './register';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Router>
      <Header /> {/* Rendered on all pages */}
      <Routes> {/* All Route components must be children of Routes */}
        <Route path="/" element={<App />} />
        <Route path="/register" element={<Register />} />
      </Routes>
      <Footer /> {/* Rendered on all pages */}
    </Router>
  </React.StrictMode>
);
