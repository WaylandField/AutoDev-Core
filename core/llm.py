import os
from enum import Enum

# Conditional imports for different LLM providers
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    import dashscope
    from dashscope import Generation
except ImportError:
    dashscope = None
    Generation = None

# 设置为 True 以跳过 API 调用，直接返回模拟数据
MOCK_MODE = False


class LLMProvider(Enum):
    OPENAI = "openai"
    QWEN = "qwen"


class LLMClient:
    def __init__(self, provider=LLMProvider.OPENAI):
        self.provider = provider
        self.MOCK_MODE = MOCK_MODE
        
        if provider == LLMProvider.OPENAI:
            self.api_key = os.getenv("OPENAI_API_KEY", "sk-xxx")
        elif provider == LLMProvider.QWEN:
            self.api_key = os.getenv("DASHSCOPE_API_KEY", "sk-df38aaf4f96d4bc6ba630d9dd57adabc")

    def chat(self, system_prompt, user_prompt):
        if self.MOCK_MODE:
            return self._mock_response(system_prompt)
        
        if self.provider == LLMProvider.OPENAI:
            return self._call_openai_api(system_prompt, user_prompt)
        elif self.provider == LLMProvider.QWEN:
            return self._call_qwen_api(system_prompt, user_prompt)
        
        return "Unsupported LLM provider"

    def _call_openai_api(self, system_prompt, user_prompt):
        """调用OpenAI API"""
        if OpenAI is None:
            raise ImportError("OpenAI package not installed. Please install it with 'pip install openai'")
        
        client = OpenAI(api_key=self.api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        
        return response.choices[0].message.content
    
    def _call_qwen_api(self, system_prompt, user_prompt):
        """调用阿里云千问API"""
        if dashscope is None or Generation is None:
            raise ImportError("DashScope package not installed. Please install it with 'pip install dashscope'")
        
        # 设置API密钥
        dashscope.api_key = self.api_key
        
        # 调用千问模型
        response = Generation.call(
            model='qwen-max',  # 使用qwen-max模型，也可以选择qwen-plus或其他千问模型
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            result_format='message'
        )
        
        if response.status_code == 200:
            return response.output.choices[0]['message']['content']
        else:
            raise Exception(f"Qwen API call failed with status code {response.status_code}: {response.message}")
    
    def _mock_response(self, system_type):
        """根据角色返回假数据用于测试流程"""
        if "Product Manager" in system_type:
            return """# Product Requirements Document

## 1. Project Overview
### Project Name
Decentralized Crowdfunding Platform

### Project Description
A blockchain-based crowdfunding platform that addresses the transparency issues of traditional crowdfunding platforms.

### Objectives and Goals
- Create a transparent crowdfunding system using blockchain technology
- Enable secure transactions with cryptocurrency
- Provide real-time visibility into fund allocation

## 2. Market Analysis
### Target Audience
- Project creators seeking funding
- Investors interested in early-stage projects
- Tech-savvy users familiar with cryptocurrencies

### Competitor Analysis
- Traditional platforms like Kickstarter lack transparency
- Existing crypto crowdfunding platforms have usability issues

### Market Opportunities
- Growing interest in blockchain technology
- Increasing adoption of cryptocurrencies

## 3. Functional Requirements
### Feature List with Priorities
1. High: Create crowdfunding campaigns
2. High: Cryptocurrency payments (USDT/ETH)
3. High: Blockchain transaction tracking
4. Medium: Campaign sharing and promotion
5. Low: User rating system

### User Stories
- As a creator, I want to create a campaign so that I can raise funds
- As an investor, I want to track my investments on the blockchain so that I can verify transparency

### Acceptance Criteria
- Campaign creation form validates all required fields
- Payments are processed securely through smart contracts
- Transaction history is visible on the blockchain

## 4. Non-functional Requirements
### Performance Requirements
- Page load time under 2 seconds
- Support for 10,000 concurrent users

### Security Requirements
- All transactions secured by smart contracts
- User data encryption

### Usability Requirements
- Intuitive UI for non-technical users
- Mobile-responsive design

## 5. Technical Requirements
### Supported Platforms
- Web browsers (Chrome, Firefox, Safari)
- Mobile devices (iOS, Android)

### Technology Stack Recommendations
- Frontend: React.js
- Backend: Node.js with Express
- Blockchain: Ethereum
- Database: PostgreSQL

### Integration Requirements
- Wallet integration (MetaMask)
- Blockchain explorer API

## 6. Project Timeline
### Milestones
1. Week 1-2: Project setup and design
2. Week 3-6: Backend development
3. Week 7-9: Frontend development
4. Week 10: Testing and deployment

### Estimated Development Time
Total: 10 weeks

### Resource Requirements
- 2 Backend developers
- 2 Frontend developers
- 1 Blockchain developer
- 1 UI/UX designer

## 7. Data Models
### Entity Relationship Diagram
User ||--o{ Campaign
Campaign ||--o{ Donation

### Data Flow Description
1. Users register and connect wallets
2. Creators create campaigns
3. Investors make donations
4. Funds are managed through smart contracts

## 8. Risk Assessment
### Potential Risks
- Regulatory changes in cryptocurrency
- Smart contract vulnerabilities
- Market volatility affecting user adoption

### Mitigation Strategies
- Regular security audits
- Compliance with evolving regulations
- Comprehensive testing of smart contracts"""
        elif "Designer" in system_type:
            return """
{ 
    "pages": [
        {"name": "Home", "components": ["HeroBanner", "CampaignList"]},
        {"name": "CreateCampaign", "components": ["FormInput", "SubmitButton"]}
    ], 
    "theme": { "primary": "#6200EE", "secondary": "#03DAC6" } 
}
"""
        elif "Architect" in system_type:
            return """
File: schema.sql
CREATE TABLE users (id SERIAL PRIMARY KEY, wallet_address VARCHAR(42) UNIQUE);
CREATE TABLE campaigns (id SERIAL PRIMARY KEY, goal DECIMAL, current DECIMAL);

File: api.yaml
openapi: 3.0.0
paths:
  /campaigns:
    get:
      summary: List all campaigns

File: contract.sol
interface ICrowdfund {
    function createCampaign(uint256 goal) external;
    function donate(uint256 campaignId) external payable;
}
"""
        elif "Full Stack Developer" in system_type:
            return """
File: src/App.js
// Start: src/App.js
import React from 'react';
export default function App() { return <h1>Crowdfund DApp</h1>; }
// End: src/App.js

File: backend/server.js
// Start: backend/server.js
const express = require('express');
const app = express();
app.listen(3000, () => console.log('Server running'));
// End: backend/server.js

File: contracts/Crowdfund.sol
// Start: contracts/Crowdfund.sol
pragma solidity ^0.8.0;
contract Crowdfund {
    struct Campaign { uint goal; uint raised; }
}
// End: contracts/Crowdfund.sol
"""
        elif "DevOps" in system_type:
            return "Dockerfile generated."
            
        return "Generic AI Response"
