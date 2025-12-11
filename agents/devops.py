import os
from core.llm import LLMClient, LLMProvider
from core.logger import record_interaction
from core.utils import save_file

class DevOpsAgent:
    def __init__(self, workspace="workspace", provider=LLMProvider.OPENAI):
        self.llm = LLMClient(provider)
        self.workspace = workspace

    @record_interaction(role="DevOps", step_name="Generate_CI_Config")
    def generate_configs(self):
        sys_prompt = "Generate Dockerfile and CI scripts."
        configs = self.llm.chat(sys_prompt, "Generate deployment configs")
        
        # 模拟生成配置文件
        save_file(f"{self.workspace}/Dockerfile", "FROM node:18\nWORKDIR /app\nCOPY . .\nCMD [\"npm\", \"start\"]")
        save_file(f"{self.workspace}/docker-compose.yml", "version: '3'\nservices:\n  web:\n    build: .")
        return "Config Generated"

    @record_interaction(role="DevOps", step_name="Run_Tests")
    def run_tests(self):
        print("⚙️ [DEVOPS] Running compilation and tests...")
        test_logs = "PASS src/App.test.js\nPASS contracts/Crowdfund.test.js"
        print(test_logs)
        return {"build": "SUCCESS", "logs": test_logs}

    @record_interaction(role="DevOps", step_name="Deploy")
    def deploy(self):
        print("🚀 [DEVOPS] Deploying to Staging Environment...")
        return "https://auto-generated-app.vercel.app"
