from rich import inspect
from rich.color import Color
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from rich.traceback import install
install(show_locals=True) # show_locals=True 会显示每个堆栈帧中的局部变量




load_dotenv()

# 创建一个对象
color = Color.parse("red")

# 查看这个对象的详细信息，包括它的方法
inspect(color, methods=True)

llm = ChatOpenAI(model = "qwen3-coder-480b-a35b-instruct",
                api_key = os.getenv("OPENAI_API_KEY"),
                base_url = os.getenv("BASE_URL")
)

inspect(llm,methods = True)


from rich.console import Console

console = Console()

try:
    # 这里是可能出错的代码
    x = 1 / 0
except Exception:
    # 打印美化后的异常信息，并显示局部变量
    console.print_exception(show_locals=True)


from rich.console import Console
from rich.table import Table

# 创建一个Console实例
console = Console()

# 创建一个表格
table = Table(title="热门编程语言")
table.add_column("名称", justify="right", style="cyan")
table.add_column("类型", style="magenta")
table.add_column("发布年份", justify="right", style="green")

table.add_row("Python", "通用", "1991")
table.add_row("JavaScript", "Web", "1995")
table.add_row("Rust", "系统", "2010")

# 通过console对象打印表格
console.print(table)
