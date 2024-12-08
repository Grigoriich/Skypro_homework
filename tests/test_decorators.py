from src.decorators import log
def test_decorator_log(capsys):
    @log(filename=None)
    def multiply(x, y):
        return x*y

    multiply(2,3)
    captured = capsys.readouterr()
    assert captured.out == "multiply ok\n"