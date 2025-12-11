import json
import time
import os
import functools
from datetime import datetime

class PromptRecorder:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

    def log(self, role, step, prompt, response, status="SUCCESS"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{role}_{step}.json"
        
        log_entry = {
            "timestamp": time.time(),
            "role": role,
            "step": step,
            "status": status,
            "prompt": prompt,
            "response": response
        }
        
        with open(os.path.join(self.log_dir, filename), "w", encoding='utf-8') as f:
            json.dump(log_entry, f, indent=4, ensure_ascii=False)
        
        print(f"📝 [LOG] Saved interaction log: {filename}")

# 全局单例
recorder = PromptRecorder()

def record_interaction(role, step_name):
    """装饰器：自动记录函数调用的 Prompt 和返回结果"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 简单处理：假设主要输入是第二个参数(args[1])，如果不存在则用全部args
            prompt_input = str(args)
            if len(args) > 1:
                prompt_input = str(args[1])
            
            try:
                result = func(*args, **kwargs)
                recorder.log(role, step_name, prompt_input, str(result), "SUCCESS")
                return result
            except Exception as e:
                recorder.log(role, step_name, prompt_input, str(e), "FAILED")
                raise e
        return wrapper
    return decorator
