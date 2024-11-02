def fibonachi(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for i in fibonachi(5):
    print(i)
