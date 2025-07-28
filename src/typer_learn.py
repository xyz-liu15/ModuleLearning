import time

import typer
from rich.progress import track


app = typer.Typer(name = "typer_learn")

@app.command()
def greeting(name: str):
    """输出问候语"""
    print(f"你好，{name}。欢迎来到Python世界！")
@app.command()
def goodbye():
    """输出结束语"""
    print("再见！")


@app.command()
def process():
    """加载进度条"""
    total = 0
    for value in track(range(100), description="进程中..."):
        # Fake processing time
        time.sleep(0.01)
        total += 1
    print(f"已加载：{total} ")






if __name__ == "__main__":
    app()