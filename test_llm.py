import os
from core.llm import LLMClient, LLMProvider

def test_llm_client():
    # 测试OpenAI提供商初始化
    openai_client = LLMClient(LLMProvider.OPENAI)
    print("OpenAI Client Provider:", openai_client.provider)
    print("OpenAI API Key:", openai_client.api_key)
    
    # 测试千问提供商初始化
    qwen_client = LLMClient(LLMProvider.QWEN)
    print("Qwen Client Provider:", qwen_client.provider)
    print("Qwen API Key:", qwen_client.api_key)
    
    # 测试聊天功能（在MOCK模式下）
    response = openai_client.chat("You are a helpful assistant.", "Hello, who are you?")
    print("Mock Response:", response[:100] + "..." if len(response) > 100 else response)

if __name__ == "__main__":
    test_llm_client()