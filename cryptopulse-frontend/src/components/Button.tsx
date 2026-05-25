import React from 'react';

interface ButtonProps {
    text: string;
    onClick: () => void;
    style?: React.CSSProperties;
}

const Button: React.FC<ButtonProps> = ({ text, onClick, style }) => {
    return (
        <button 
            onClick={onClick} 
            style={{ 
                backgroundColor: '#4A90E2', 
                color: '#FFFFFF', 
                border: 'none', 
                borderRadius: '5px', 
                padding: '10px 20px', 
                cursor: 'pointer', 
                ...style 
            }}
        >
            {text}
        </button>
    );
};

export default Button;