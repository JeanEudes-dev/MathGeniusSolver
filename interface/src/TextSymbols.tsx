// Symbols.tsx
import React from 'react';
import { texSymbols } from './texSymbols';

interface SymbolProps {
    icon: string;
    data: string;
    onClick: (data: string) => void;
}

const Symbol: React.FC<SymbolProps> = ({ icon, data, onClick }) => (
    <button title="button" type="button" className="tex-button" onClick={() => { console.log(data); onClick(data); }}>
        <i className={icon}></i>
    </button>
);



interface SymbolsProps {
    onClick: (data: string) => void;
}

const TextSymbols: React.FC<SymbolsProps> = ({ onClick }) => {
    const buttonNodes = texSymbols.map((symbol) => (
        <Symbol key={symbol.data} icon={symbol.icon} data={symbol.data} onClick={onClick} />
    ));

    return (
        <div style={{ display: 'grid', gridAutoFlow: 'column', gridTemplateRows: 'auto auto', gridGap: 5 }}>
            {buttonNodes}
        </div>
    );
};

export default TextSymbols;
