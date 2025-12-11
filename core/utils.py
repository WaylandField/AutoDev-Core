import os

def save_file(filepath, content):
    """自动创建目录并保存文件"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"💾 [FILE] Generated: {filepath}")

def parse_code_blocks(llm_response):
    """
    简单的解析器：从 LLM 返回的文本中提取文件名和代码内容
    假设格式包含 '// Start: filename' 和 '// End: filename' 标记 (对应 llm.py 中的 mock)
    """
    files = {}
    
    # 简单的文本分割逻辑 (仅适配 llm.py 中的 mock 数据格式)
    lines = llm_response.split('\n')
    current_file = None
    buffer = []
    
    for line in lines:
        if "// Start: " in line:
            current_file = line.split("// Start: ")[1].strip()
            buffer = []
        elif "// End: " in line and current_file:
            files[current_file] = "\n".join(buffer)
            current_file = None
        elif current_file:
            buffer.append(line)
            
    # 如果没解析到特殊标记，但有内容，做一个兜底 (主要用于真实 LLM 返回不规范时)
    if not files and len(llm_response) > 0:
        # 这里仅为演示，不作实际处理
        pass
        
    return files
