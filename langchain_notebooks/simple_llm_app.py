from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from rich import print




# 获取API密钥和接口地址
zhipu_api_key = os.getenv("OPENAI_API_KEY")
zhipu_base_url = os.getenv("BASE_URL")

# 实例化大模型
model = ChatOpenAI(
    model = "glm-4.5-flash",
    api_key = zhipu_api_key,
    base_url = zhipu_base_url
)

prompt_template = """
你是一个宣传标语专家，请根据用户需求设计一个独具创意且引人注目的宣传标语，需结合该产品/活动的核心价值和特点，同时融入新颖的表达方式或视角。
请确保标语能够激发潜在客户的兴趣，并能留下深刻印象，可以考虑采用比喻、双关或其他修辞手法来增强语言的表现力。
标语应简洁明了，需要朗朗上口，易于理解和记忆，一定要押韵，不要太过书面化。只输出宣传标语，不用解释。
请对{topic}写一个宣传标语。
"""

prompt = ChatPromptTemplate.from_messages(
    [("system",prompt_template),
    ("user","{query}")
    ]
)


chain = prompt | model | StrOutputParser()

for chunk in chain.stream({"query": "苹果","topic" : "出售苹果"}):
    print(chunk,end = "",flush = True)