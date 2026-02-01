"""
@Author : 顾清歌
@Time : 2026/1/28 22:20
@Description: 
"""
from typing import Optional, List
import time
import typer
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from concurrent.futures import ThreadPoolExecutor

app = typer.Typer()

@app.command()
def greet(name: str, times: int = 1, loud: bool = False):
    for i in range(times):
        if loud:
            print(f"HELLO, {name.upper()}!")
        else:
            print(f"Hello, {name}")


@app.command()
def count(files: List[str], count_lines: bool = False):
    # 1. 用 partial 固定 count_lines 参数
    task = partial(count_one, count_lines=count_lines)

    # 2. 用线程池并发执行
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(task, files)

    # 3. 打印结果
    for result in results:
        print(result)



def count_one(file: str, count_lines: bool) -> str:
    try:
        with open(file, "r") as f:
            content = f.read()
            time.sleep(1)  # 模拟耗时操作
            if count_lines:
                return f"{file}: {len(content.splitlines())}"
            else:
                return f"{file}: {len(content)}"
    except FileNotFoundError:
        return f"{file}: ERROR - 文件不存在"
    except PermissionError:
        return f"{file}: ERROR - 权限不足"
    except OSError as e:
        return f"{file}: ERROR - {e}"


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

