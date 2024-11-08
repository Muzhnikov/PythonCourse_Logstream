from random import shuffle

def shuffle_list(l):
    shuffle(l)
    return l

not_shuf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(shuffle_list(not_shuf))
