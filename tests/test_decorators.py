from src.decorators import log

def test_decorator_log(capsys):
    @log(filename=None)
    def multiply(x, y):
        return x*y

    multiply(2,3)
    captured = capsys.readouterr()
    assert captured.out == "multiply ok\n"


def test_decorator_log_exception(capsys):
    @log(filename=None)
    def multiply(x, y):
        raise ValueError("Недопустимые значения")

    multiply(2,3)
    captured = capsys.readouterr()
    assert captured.out == "multiply error: Недопустимые значения. Inputs: (2, 3), {}\n"

def test_decorator_log_to_file():
    @log(filename="text.txt")
    def multiply(x, y):
        return x*y

    multiply(2,3)
    with open("text.txt", 'r') as file:
        content = file.readlines()
    assert content[-1] == "multiply ok\n"


def test_decorator_log_to_file_exception():
    @log(filename="text.txt")
    def multiply(x, y):
        raise ValueError("Недопустимые значения")

    multiply(2,3)
    with open("text.txt", 'r') as file:
        content = file.readlines()
    assert content[-1] == "multiply error: Недопустимые значения. Inputs: (2, 3), {}\n"