/* eslint-disable @typescript-eslint/no-unused-vars */
import React, { useState } from 'react';
import { addStyles, EditableMathField } from 'react-mathquill';

import TexSymbols from './TextSymbols';
import { Card, Flex } from 'antd';

addStyles();

const Inputs: React.FC<{ onInputChange: (formula: string) => void }> = ({ onInputChange }) => {
  const [formula, setFormula] = useState('');

  function handleChange(mathField: { latex: () => string }) {
    setFormula(mathField.latex());
    onInputChange(mathField.latex());
    console.log(mathField)
  }

  function handleInsertSymbol(symbol: string) {
    setFormula((oldFormula) => oldFormula + symbol);
  }

  return (
    <Card style={{ width: '600px' }} title="Input Formula">
      <Flex gap={"middle"} vertical>
        <EditableMathField latex={formula} onChange={handleChange} />
        <hr />
        <TexSymbols onClick={handleInsertSymbol} />
      </Flex>
      
    </Card>
  );
};

export default Inputs;
