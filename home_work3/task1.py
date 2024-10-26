def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Ошибка! На ноль делить нельзя.")
    return x / y

def power(x, y):
    return x ** y

def check_input(user_input):
    try:
        return float(user_input)
    except ValueError:
        raise ValueError("Ошибка! Введите корректное число.")

def calculator():
    print("Начало работы.")
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Выход из программы")

        try:
            operation = int(input("Введите номер операции: "))
            if operation == 6:
                print("Завершение работы.")
                break
            elif operation not in [1, 2, 3, 4, 5]:
                print("Ошибка! Такой операции нет.")
                continue

            x = check_input((input("Введите первое число: ")))
            y = check_input((input("Введите второе число: ")))

            if operation == 1:
                print("Результат:", add(x, y))
            elif operation == 2:
                print("Результат:", subtract(x, y))
            elif operation == 3:
                print("Результат:", multiply(x, y))
            elif operation == 4:
                print("Результат:", divide(x, y))
            elif operation == 5:
                print("Результат:", power(x, y))

        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)

calculator()
