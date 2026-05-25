import React from 'react';
import HeroSection from '../components/HeroSection';
import Navbar from '../components/Navbar';

const Home: React.FC = () => {
    return (
        <div className="home">
            <Navbar />
            <HeroSection />
        </div>
    );
};

export default Home;