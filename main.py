import os
from agents.pm import PMAgent
from agents.designer import DesignerAgent
from agents.architect import ArchitectAgent
from agents.backend_dev import BackendDeveloperAgent
from agents.frontend_dev import FrontendDeveloperAgent
from agents.devops import DevOpsAgent
from core.llm import LLMProvider

def main():
    print("==================================================")
    print("🤖 AutoDev-Core: AI Automated Development Framework")
    print("==================================================\n")

    user_requirement = input("请输入您的需求 (回车默认: '集群监控平台'): ") or "集群监控平台"
    llm_choice = input("请选择LLM提供商 (1: 阿里云千问, 2: OpenAI, 默认: 1): ") or "1"
    workspace = "workspace_output"
    
    # 选择LLM提供商
    provider = LLMProvider.QWEN if llm_choice == "1" else LLMProvider.OPENAI
    
    # 初始化
    pm = PMAgent(provider)
    designer = DesignerAgent(provider)
    architect = ArchitectAgent(provider)
    backend_dev = BackendDeveloperAgent(workspace=workspace, provider=provider)
    frontend_dev = FrontendDeveloperAgent(workspace=workspace, provider=provider)
    devops = DevOpsAgent(workspace=workspace, provider=provider)

    try:
        print("\n[Step 1] PM Agent Analyzing...")
        prd = pm.analyze(user_requirement)
        
        # 保存PRD到代码目录
        prd_filepath = os.path.join(workspace, "PRD.md")
        with open(prd_filepath, 'w', encoding='utf-8') as f:
            f.write(prd)
        print(f"✅ PRD saved to '{prd_filepath}'")
        
        print("\n[Step 2] Design Agent Working...")
        design = designer.design_ui(prd)
        
        print("\n[Step 3] Architect Defining Specs...")
        specs = architect.define_specs(prd, prd)
        
        print("\n[Step 4] Backend Developer Writing Code...")
        backend_files = backend_dev.implement_backend_code(specs)
        print(f"✅ Generated {len(backend_files)} backend files in '{workspace}/'")
        
        print("\n[Step 5] Frontend Developer Writing Code...")
        frontend_files = frontend_dev.implement_frontend_code(specs)
        print(f"✅ Generated {len(frontend_files)} frontend files in '{workspace}/'")
        
        # 合并文件列表
        files = backend_files + frontend_files
        
        print("\n[Step 6] DevOps Building & Deploying...")
        devops.generate_configs()
        devops.run_tests()
        url = devops.deploy()
        
        print(f"\n✨ Success! Deployed at: {url}")
        print(f"📄 Check 'logs/' for prompt history.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
