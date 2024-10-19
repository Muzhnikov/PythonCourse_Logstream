dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
set_keys = set()
set_values = set()

for key, value in dct.items():
    set_keys.add(key)
    set_values.add(value)

set_all = set_keys | set_values
print(set_all)