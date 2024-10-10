user_input = input("Введите число: ")
positive_sum = 0
negative_sum = 0

if user_input.isdigit():
    number = int(user_input)
    for i in range(-number, number + 1):
        print(i, end="\t")
        if i > 0:
            positive_sum += i
        elif i < 0:
            negative_sum += i
    print()
    print(f"Сумма положительных чисел: {positive_sum}")
    print(f"Сумма отрицательных чисел: {negative_sum}")
else:
    print("Введено не число.")