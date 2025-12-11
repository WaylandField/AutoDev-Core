from core.llm import LLMClient, LLMProvider
from core.logger import record_interaction

class DesignerAgent:
    def __init__(self, provider=LLMProvider.OPENAI):
        self.llm = LLMClient(provider)

    @record_interaction(role="Designer", step_name="Generate_Figma_Spec")
    def design_ui(self, prd_content):
        sys_prompt = "You are a UI/UX Designer. Output a JSON structure describing the Figma layers based on the PRD."
        design_json_str = self.llm.chat(sys_prompt, prd_content)
        return design_json_str
