from core.llm import LLMClient, LLMProvider
from core.logger import record_interaction

class ArchitectAgent:
    def __init__(self, provider=LLMProvider.OPENAI):
        self.llm = LLMClient(provider)

    @record_interaction(role="Architect", step_name="Generate_Specs")
    def define_specs(self, prd, design_spec):
        sys_prompt = "You are a Solution Architect. Output DB Schema, API YAML, and Smart Contract Interface."
        return self.llm.chat(sys_prompt, f"PRD: {prd}\nDesign: {design_spec}")
