#from itertools import permutations
while True:
    user_input = input("Введите трехзначное число, в котором все цифры различны или exit для выхода: ")

    if user_input.lower() == "exit":
        print("Программа завершена.")
        break

    if len(user_input) == 3 and user_input.isdigit():
        if len(set(user_input)) == 3:
            # в общем случае надо конечно делать через permutations:
            # for i in permutations(user_input):
            #     print (*i)
            # но тут я так понимаю от нас хотят такой вариант:
            a, b, c = user_input[0], user_input[1], user_input[2]
            print("Все возможные перестановки цифр:")
            print(a + b + c)
            print(a + c + b)
            print(b + a + c)
            print(b + c + a)
            print(c + a + b)
            print(c + b + a)
        else:
            print(f"В числе {user_input} есть повторяющиеся цифры.")
    else:
        print("Введено не число. Пожалуйста, введите число.")