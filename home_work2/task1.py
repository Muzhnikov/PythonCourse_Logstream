degree = int(input("Введите степень: "))
n = int(input("Введите количество элементов: "))
l = []

for i in range(n):
    new_el = input("Введите элемент списка: ")

    if (new_el.replace('.', '', 1).replace('-', '', 1).isdigit()
            and (new_el.count('-') == 0 or (new_el.count('-') == 1 and new_el[0] == '-'))
            and new_el[0] != '.'):
        ch = float(new_el)
        l.append(ch ** degree)
    else:
        l.append(new_el * degree)

print(l)