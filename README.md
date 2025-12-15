## AutoDev-Core 多agent模型来模拟一个完整的开发团队，每个代理负责软件开发的特定方面，代理支持OpenAI GPT和阿里云千问模型
### agent角色包括：
- 产品经理（PM）代理 - 将模糊的想法转化为详细的产品需求文档（PRD）
- 设计代理 - 根据需求创建UI/UX设计，转化为figma json设计
- 架构师代理 - 设计系统架构、数据库模式和API
- 后端开发代理 - 生成后端代码和服务
- 前端开发代理 - 创建响应式前端界面
- 运维代理 - 处理部署、测试和CI/CD配置
### 后续：
1. 需要对promt 进行进一步精细化管理；
2. 需要增加一个router，规划多agent路径；
3. 后续可以继续补充其他agent，比如智能合约开发agent；
4. 


## AutoDev-Core uses a multi-agent model to simulate a complete software development team. Each agent is responsible for a specific aspect of the software development lifecycle. The agents support both OpenAI GPT models and Alibaba Cloud Qwen models.

### Agent Roles Include:

Product Manager (PM) Agent – Transforms vague ideas into detailed Product Requirement Documents (PRDs)

Design Agent – Creates UI/UX designs based on requirements and converts them into Figma JSON designs

Architect Agent – Designs system architecture, database schemas, and APIs

Backend Developer Agent – Generates backend code and services

Frontend Developer Agent – Builds responsive frontend interfaces

DevOps Agent – Handles deployment, testing, and CI/CD configuration

### Next Steps:

Further refine and systematically manage prompts

Introduce a router to plan and orchestrate multi-agent execution paths

Gradually add more agents, such as a Smart Contract Development Agent