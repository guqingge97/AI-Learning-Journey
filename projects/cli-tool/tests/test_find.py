import pytest
from typer.testing import CliRunner
from cli_tool.main import app

runner = CliRunner()


class TestFind:
    """find 命令测试"""

    def test_find_keyword_exists(self, tmp_path):
        """正常：关键词存在"""
        f = tmp_path / "test.txt"
        f.write_text("hello world\nfoo bar\nhello again\n")

        result = runner.invoke(app, ["find", "hello", str(f)])

        assert result.exit_code == 0
        assert "hello" in result.stdout

    def test_find_file_not_found(self, tmp_path):
        """异常：文件不存在"""
        fake_path = tmp_path / "not_exist.txt"

        result = runner.invoke(app, ["find", "keyword", str(fake_path)])

        assert result.exit_code == 1

    def test_find_keyword_not_exists(self, tmp_path):
        """边界：关键词不存在"""
        f = tmp_path / "test.txt"
        f.write_text("hello world\nfoo bar\n")

        result = runner.invoke(app, ["find", "xyz", str(f)])

        assert result.exit_code == 0
        assert result.stdout == "" or "xyz" not in result.stdout