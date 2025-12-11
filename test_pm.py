import sys
import os
sys.path.append('/Users/wayland/workspace/python/auto-factory/AutoDev-Core')

from agents.pm import PMAgent
from core.llm import LLMProvider

def test_pm_enhancement():
    # 创建PM代理实例
    pm_agent = PMAgent(provider=LLMProvider.OPENAI)
    
    # 测试需求分析功能
    requirement = "众筹平台"
    print("Generating PRD for requirement:", requirement)
    
    # 生成PRD
    prd = pm_agent.analyze(requirement)
    
    # 打印PRD的前500个字符以验证内容
    print("\nGenerated PRD (first 500 characters):")
    print(prd[:500] + "..." if len(prd) > 500 else prd)
    
    # 验证PRD是否包含预期的部分
    expected_sections = [
        "Project Overview",
        "Market Analysis", 
        "Functional Requirements",
        "Non-functional Requirements",
        "Technical Requirements"
    ]
    
    print("\nValidation Results:")
    for section in expected_sections:
        if section in prd:
            print(f"✓ {section} - Found")
        else:
            print(f"✗ {section} - Not found")

if __name__ == "__main__":
    test_pm_enhancement()