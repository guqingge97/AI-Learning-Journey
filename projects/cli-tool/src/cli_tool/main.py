"""
@Author : 顾清歌
@Time : 2026/1/28 22:20
@Description: 
"""
from typing import Optional

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
    try:
        with open(file, "r") as f:
            # 真正的业务逻辑放这里
            if count_lines:
                print(len(f.readlines()))
            else:
                print(len(f.read().split()))
    except FileNotFoundError:
        typer.echo(f"Error: 文件 '{file}' 不存在", err=True)
        raise typer.Exit(code=1)
    except PermissionError:
        typer.echo(f"Error: 没有权限读取 '{file}'", err=True)
        raise typer.Exit(code=1)
    except OSError as e:
        typer.echo(f"Error: 读取文件失败 - {e}", err=True)
        raise typer.Exit(code=1)



@app.command()
def find(char: str, file: str):
    """查找关键词"""
    try:
        with open(file, "r") as f:
            for line in f:
                if char in line:
                    print(line)
    except FileNotFoundError:
        typer.echo(f"Error: 文件 '{file}' 不存在", err=True)
        raise typer.Exit(code=1)
    except PermissionError:
        typer.echo(f"Error: 没有权限读取 '{file}'", err=True)
        raise typer.Exit(code=1)
    except OSError as e:
        typer.echo(f"Error: 读取文件失败 - {e}", err=True)
        raise typer.Exit(code=1)

@app.command()
def replace(source: str, target: str, file: str, output: Optional[str] = None):
    """批量替换文本"""
    try:
        if output:
            with open(file, "r") as f, open(output, "w") as f2:
                for line in f:
                    f2.write(line.replace(source, target))
        else:
            with open(file, "r") as f:
                for line in f:
                    print(line.replace(source, target))
    except FileNotFoundError:
        typer.echo(f"Error: 文件 '{file}' 不存在", err=True)
        raise typer.Exit(code=1)
    except PermissionError:
        typer.echo(f"Error: 没有权限读取 '{file}'", err=True)
        raise typer.Exit(code=1)
    except OSError as e:
        typer.echo(f"Error: 读取文件失败 - {e}", err=True)
        raise typer.Exit(code=1)






if __name__ == "__main__":
    app()

