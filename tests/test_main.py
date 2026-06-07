from src.main import add, format_task

def test_add():
    assert add(2, 3) == 6

def test_format_task():
    assert format_task("build", "done") == "[DONE] build"
