from agentscope.message import Msg
from rich.console import Console


console = Console()

messages = Msg(
    name = "Python编程专家",
    role = "system",
    content = "你是一个顶级Python专家，拥有关于Python所有模块的最先进的知识，可以使用中文对用户进行教导。"
)


console.print(messages)