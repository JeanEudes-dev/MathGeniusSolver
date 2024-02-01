import React from 'react';
import { Card, Typography } from 'antd';

const { Title } = Typography;

interface OutputProps {
  result: string | null;
}

const Output: React.FC<OutputProps> = ({ result }) => {
  return (
    <Card
      style={{ width: 600, marginLeft: 'auto', marginRight: 'auto' }}
      title={
        <Title level={4}>Output</Title>
      }
    >
      {result}
    </Card>
  );
};

export default Output;
