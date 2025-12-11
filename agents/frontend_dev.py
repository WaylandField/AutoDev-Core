import os
from core.llm import LLMClient, LLMProvider
from core.logger import record_interaction
from core.utils import save_file, parse_code_blocks


class FrontendDeveloperAgent:
    def __init__(self, workspace="workspace", provider=LLMProvider.OPENAI):
        self.llm = LLMClient(provider)
        self.workspace = workspace

    @record_interaction(role="Frontend_Dev", step_name="Generate_Frontend_Code")
    def implement_frontend_code(self, specs):
        sys_prompt = "You are a Frontend Developer. Write frontend code based on specs. Focus on UI components, user interactions, and client-side logic. Use '// Start: filename' markers."
        
        # 1. 获取 LLM 响应
        raw_response = self.llm.chat(sys_prompt, f"Specifications: {specs}")
        
        # 2. 解析文件
        if self.llm.MOCK_MODE:
            # 使用 utils 中的解析逻辑解析 mock 数据
            parsed_files = parse_code_blocks(raw_response)
        else:
            parsed_files = parse_code_blocks(raw_response)
            
        # 3. 写入文件
        created_paths = []
        for rel_path, content in parsed_files.items():
            # 只处理前端相关文件
            if rel_path.startswith(("src/", "public/", "assets/")):
                full_path = os.path.join(self.workspace, rel_path)
                save_file(full_path, content)
                created_paths.append(full_path)
            
        return created_paths