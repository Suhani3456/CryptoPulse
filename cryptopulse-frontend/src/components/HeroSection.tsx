import React from 'react';
import Button from './Button';

const HeroSection: React.FC = () => {
    return (
        <div className="hero-section" style={{ background: 'linear-gradient(135deg, #1a1a2e, #16213e)', color: '#ffffff', padding: '50px 20px', textAlign: 'center' }}>
            <h1>Track Your Crypto Assets in Real-Time</h1>
            <div style={{ marginTop: '20px' }}>
                <Button text="Get Started" onClick={() => console.log('Get Started clicked')} />
                <Button text="View Dashboard" onClick={() => console.log('View Dashboard clicked')} />
            </div>
        </div>
    );
};

export default HeroSection;