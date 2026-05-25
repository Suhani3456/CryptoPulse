import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css'; // Assuming you will create a CSS file for Navbar styles

const Navbar: React.FC = () => {
    return (
        <nav className="navbar">
            <div className="navbar-brand">CryptoPulse</div>
            <ul className="navbar-links">
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/dashboard">Dashboard</Link>
                </li>
                <li>
                    <Link to="/portfolio">Portfolio</Link>
                </li>
                <li>
                    <Link to="/analytics">Analytics</Link>
                </li>
            </ul>
        </nav>
    );
};

export default Navbar;