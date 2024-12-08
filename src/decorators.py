
def log(filename=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if not filename:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, 'w') as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
            else:
                if not filename:
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, 'w') as file:
                        file.write(f"{func.__name__} ok\n")
                return result
        return wrapper
    return my_decorator