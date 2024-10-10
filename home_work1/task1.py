while True:
    user_input = input("Введите число или exit для выхода: ")

    if user_input.lower() == "exit":
        print("Программа завершена.")
        break

    if user_input.isdigit() or (user_input[1:].isdigit() and int(user_input) < 0):
        if int(user_input) < 0:
            user_input = user_input[1:]
        print(f"Длина введенного числа: {len(user_input)}")
    else:
        print("Введено не число. Пожалуйста, введите число.")