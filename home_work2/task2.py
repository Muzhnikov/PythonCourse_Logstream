s = input("Введите строку: ").lower()
d = {}

for ch in s:
    if ch != ' ' and ch not in d:
        d[ch] = s.count(ch)
print(d)