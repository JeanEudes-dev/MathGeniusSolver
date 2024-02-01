import React, { useState } from 'react';
import { Breadcrumb, Layout, Input, Button, Select, Typography, theme, Flex } from 'antd';
import Inputs from './Inputs';
import Output from './Output';

const { Header, Content, Footer } = Layout;
const { Option } = Select;
const { Title } = Typography;


const Layouts: React.FC = () => {
    const {
        token: { colorBgContainer, borderRadiusLG },
    } = theme.useToken();

    const [selectedCategory, setSelectedCategory] = useState<string>('algebra');
    const [mathProblem, setMathProblem] = useState<string>('');
    const [result, setResult] = useState<string | null>(null);

    const handleCategoryChange = (value: string) => {
        setSelectedCategory(value);
    };

    const handleInputChange = (input: string) => {
        setMathProblem(input);
    };

    const handleSolveClick = () => {

        setResult('42');
    };

    return (
        <Layout>
            <Header style={{ display: 'flex', alignItems: 'center', color: '#ffff', textAlign: 'center' }}>
                <h1>MathGeniusSolver</h1>

            </Header>
            <Content style={{ padding: '0 48px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item>Home</Breadcrumb.Item>
                    <Breadcrumb.Item>Math Problem Solver</Breadcrumb.Item>
                </Breadcrumb>
                <div
                    style={{
                        background: colorBgContainer,
                        minHeight: 280,
                        padding: 24,
                        borderRadius: borderRadiusLG,
                    }}
                >
                    <Title level={2} style={{ marginBottom: 24 }}>
                        Math Problem Solver
                    </Title>
                    <Select
                        style={{ width: 200, marginBottom: 16 }}
                        defaultValue={selectedCategory}
                        onChange={handleCategoryChange}
                    >
                        <Option value="algebra">Algebra</Option>
                        <Option value="trigonometry">Trigonometry</Option>
                    </Select>
                    <Flex gap={"middle"}>
                        <Inputs onInputChange={handleInputChange} />
                        <Output />
                    </Flex>
                </div>
            </Content>
            <Footer style={{ textAlign: 'center' }}>
                Ant Design ©{new Date().getFullYear()} Created by Ant UED
            </Footer>
        </Layout>
    );
};

export default Layouts;