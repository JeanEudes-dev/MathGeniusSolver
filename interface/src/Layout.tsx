import React, { useState } from 'react';
import { Breadcrumb, Layout, Button, Select, Typography, theme, Flex } from 'antd';
import Inputs from './Inputs';
import Output from './Output';
import axios from 'axios';

const { Header, Content, Footer } = Layout;
const { Option } = Select;
const { Title } = Typography;


type result = {
    result: string;
    explanation: string;
}


const Layouts: React.FC = () => {
    const {
        token: { colorBgContainer, borderRadiusLG },
    } = theme.useToken();

    const [selectedCategory, setSelectedCategory] = useState<string>('algebra');
    const [mathProblem, setMathProblem] = useState<string>('');
    const [result, setResult] = useState<result>({ explanation: "", result: "" });

    const handleCategoryChange = (value: string) => {
        setSelectedCategory(value);
    };

    const handleInputChange = (input: string) => {
        setMathProblem(input);
        console.log(input)
    };

    const handleSolveClick = async () => {
        if (!mathProblem || selectedCategory === '') return;
        try {
            // eslint-disable-next-line no-undef
            const response = await axios.post(`http://localhost:8000/api/solve/algebra/`, { expression: mathProblem });
            setResult(response.data);
            console.log(response)
        } catch (error) {
            console.error(error);
        }
        // setResult('42');
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
                        <Output result={result} />
                    </Flex>
                    <Button type='primary' className='button' onClick={handleSolveClick}>Solve</Button>
                </div>
            </Content>
            <Footer style={{ textAlign: 'center' }}>
                Ant Design ©{new Date().getFullYear()} Created by Ant UED
            </Footer>
        </Layout>
    );
};

export default Layouts;