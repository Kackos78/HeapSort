# bubble_sort
from time import time
from random import randint
def list_gen(mi=-100, ma=100, le=100):
    return [randint(mi, ma) for i in range(le)]

def algo_time(func, x):
 start = time()
 func(x)
 finish = time() - start
 print(f'Выполнение за {finish} сек.')


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
