# Задание 2 (тайминг 20 минут)
# 1.Написать алгоритм быстрой сортировки (quicksort).

from random import randint
from time import time


def list_gen(mi=-5, ma=5, le=10):
    return [randint(mi, ma) for i in range(le)]


def algo_time(func, x):
    start = time()
    func(x)
    finish = time() - start
    print(f"Выполение за {finish} сек.")


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = list(filter(lambda x: x < pivot, lst))
    center = [i for i in lst if i == pivot]
    right = list(filter(lambda x: x > pivot, lst))
    return quick_sort(left) + center + quick_sort(right)


my_list = list_gen()

print(my_list)
my_list_sorted = quick_sort(my_list)
print(my_list_sorted)
