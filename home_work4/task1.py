# 1. список квадратов первых 10 натуральных чисел
square_list = [i**2 for i in range(1, 11)]
print(square_list)

# 2. словарь, содержащий названия дней недели и их порядковые номера
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekdays_dict = {day: i + 1 for i, day in enumerate(days)}
print(weekdays_dict)

# 3. множество, содержащее теги библиотек в нижнем регистре
libs = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
libs_set = {lib.lower() for lib in libs}
print(libs_set)
