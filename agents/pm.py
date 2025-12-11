from core.llm import LLMClient, LLMProvider
from core.logger import record_interaction

class PMAgent:
    def __init__(self, provider=LLMProvider.OPENAI):
        self.llm = LLMClient(provider)

    @record_interaction(role="PM", step_name="Expand_Requirements")
    def analyze(self, raw_requirement):
        sys_prompt = '''You are an expert Product Manager. Your task is to create a comprehensive PRD (Product Requirements Document) based on the user's requirement. The PRD should be in Markdown format and include the following sections:
        
1. Project Overview
   - Project Name
   - Project Description
   - Objectives and Goals
   
2. Market Analysis
   - Target Audience
   - Competitor Analysis
   - Market Opportunities
   
3. Functional Requirements
   - Feature List with Priorities
   - User Stories for each Feature
   - Acceptance Criteria
   
4. Non-functional Requirements
   - Performance Requirements
   - Security Requirements
   - Usability Requirements
   
5. Technical Requirements
   - Supported Platforms
   - Technology Stack Recommendations
   - Integration Requirements
   
6. Project Timeline
   - Milestones
   - Estimated Development Time
   - Resource Requirements
   
7. Data Models
   - Entity Relationship Diagram (in text form)
   - Data Flow Description
   
8. Risk Assessment
   - Potential Risks
   - Mitigation Strategies'''
        return self.llm.chat(sys_prompt, raw_requirement)
