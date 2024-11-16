def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num)/len(list_num), 2)

assert average_num([2, 2, 2]) == 2
assert average_num([1, "2", 3]) == 2
assert average_num([1, "fff", 3]) == "Bad request"
assert average_num([1.5, "2.5", 4.5]) == "Bad request"
assert average_num([1.0, 2.0, 3.0, 4.0]) == 2.5
assert average_num([100000000000000, 200000000000000, 300000000000000, 400000000000000]) == 250000000000000
assert average_num([-1, -2, -3]) == -2.0
assert average_num([1, 2, -3]) == 0
assert average_num([1.5, 2, -3.5, -4]) == -1
