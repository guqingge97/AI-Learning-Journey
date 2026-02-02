import pytest
from typer.testing import CliRunner
from cli_tool.main import app

runner = CliRunner()


class TestCount:
    """count 命令测试"""

    def test_count_lines_normal(self, tmp_path):
        """正常：统计文件行数"""
        f = tmp_path / "test.txt"
        f.write_text("line1\nline2\nline3\n")

        result = runner.invoke(app, ["count", "--count-lines", str(f)])

        assert result.exit_code == 0
        assert ": 3" in result.stdout

    def test_count_file_not_found(self, tmp_path):
        """异常：文件不存在"""
        fake_path = tmp_path / "not_exist.txt"

        result = runner.invoke(app, ["count", str(fake_path)])

        assert "ERROR" in result.stdout or "不存在" in result.stdout

    def test_count_empty_file(self, tmp_path):
        """边界：空文件"""
        f = tmp_path / "empty.txt"
        f.write_text("")

        result = runner.invoke(app, ["count", "--count-lines", str(f)])

        assert result.exit_code == 0
        assert ": 0" in result.stdout