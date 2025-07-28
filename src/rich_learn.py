"""
rich模块的使用
需要使用uv add rich进行安装。
"""
from rich.console import Console


console = Console()
console.print("[bold red]你好！！！[/bold red]")


my_list = [1,2,3,4,5,6,7,8,9,10]
my_dict = {"name" : "LiHua","age" : 23}

console.print(my_list)
console.print(my_dict)