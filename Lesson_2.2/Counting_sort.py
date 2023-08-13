from time import time
from random import randint

def list_gen(mi=-5, ma=5, le=10):
    return [randint(mi, ma) for i in range(le)]

def counting_sort(list):
    max_item = max(list)
    new_list = [0 for _ in range(max_item + 1)]
    for i in list:
        new_list[i] = new_list[i] + 1
    print(new_list)
    res_sp = []
    for i in range(len(new_list)):
        if new_list[i]:
            res_sp.extend([i] * new_list[i])
    print(res_sp)

my_list = list_gen()
print(my_list)
sort_list = counting_sort(my_list)
# print(sort_list)