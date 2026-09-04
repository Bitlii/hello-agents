import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件中的环境变量
load_dotenv()

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

# 示例调用
# 输入文本和图像 URL
# 输出文本
completion = client.chat.completions.create(
    model=os.getenv("LLM_MODEL_ID"),
    messages=[{"role": "user", "content": [
        {"type": "image_url",
         "image_url": {"url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"}},
        {"type": "text", "text": "这是什么"},
    ]}]
)
print(completion.model_dump_json())

