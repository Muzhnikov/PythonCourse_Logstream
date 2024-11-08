import my_module

r = 5
s = my_module.circle_area(5)
print(f"Площадь круга радиса {r}: {s}")

grades = [4, 5, 3, 4, 5]
avg = my_module.average_score(grades)
print(f"Средний балл для оценок {grades}: {avg}")

money = 1800
amount = my_module.sber_count_securities(money)
print(f"На сумму {money} рублей можно купить {amount} акций сбера")
