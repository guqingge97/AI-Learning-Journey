"""
@Author : 顾清歌
@Time : 2026/1/28 22:20
@Description: 
"""

import typer

app = typer.Typer()

@app.command()
def greet(name: str, times: int = 1, loud: bool = False):
    for i in range(times):
        if loud:
            print(f"HELLO, {name.upper()}!")
        else:
            print(f"Hello, {name}")




@app.command()
def count(file: str, count_lines: bool = False):
    """统计文件字数/行数"""
    with open(file, "r") as f:
        if count_lines:
            print(len(f.readlines()))
        else:
            print(len(f.read().split()))



@app.command()
def find(char: str, file: str):
    """查找关键词"""
    with open(file, "r") as f:
        for line in f:
            if char in line:
                print(line)

@app.command()
def replace(source: str, target: str, file: str):
    """批量替换文本"""
    with open(file, "r") as f:
        for line in f:
            if source in line:
                line = line.replace(source, target)
                print(line)





if __name__ == "__main__":
    app()

