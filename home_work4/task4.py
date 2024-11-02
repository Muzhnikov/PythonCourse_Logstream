def decor(func):
    def wrapper(*args, **kwargs):
        print(f"Имя функции: {func.__name__}")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decor
def fibonachi(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in fibonachi(5):
    print(i)
