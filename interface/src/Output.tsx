import React from 'react';
import { Card, Typography } from 'antd';

const { Title } = Typography;

interface OutputProps {
  result: {
    result: string;
    explanation: string;
  }
}

const Output: React.FC<OutputProps> = ({ result }) => {
  return (
    <Card
      style={{ width: 600, marginLeft: 'auto', marginRight: 'auto' }}
      title={
        <Title level={4}>Output</Title>
      }
    >
      <Typography.Paragraph>{result.result}</Typography.Paragraph>
      <Typography.Paragraph type="secondary">{result.explanation}</Typography.Paragraph>
    </Card>
  );
};

export default Output;
