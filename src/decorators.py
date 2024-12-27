from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Callable:
    "Декоратор, логирующий успешность выполнения функции в консоль или файл"

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: tuple) -> Any:
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if not filename:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
            else:
                if not filename:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok\n")
                return result

        return wrapper

    return my_decorator
