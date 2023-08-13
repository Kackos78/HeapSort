# Задание 1
# 1.Необходимо написать один из простых алгоритмов сортировки,
# имеющий сложность O(n2).
# 2.Можно выбрать из пузырьковой сортировки, сортировки вставками и
# сортировки выбором.
# 3.Следует обратить внимание на сложность данных алгоритмов и
# указать признаки квадратичной сложности для каждого из них.
from random import randint
from time import time

array = [9, 8, 7, 6, 5, 4, 3, 2, 1]


# bable_sort
def arretSort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def algo_time(func, x):
    start = time()
    func(x)
    finish = time() - start
    print(f"Выполение за {finish} сек.")


algo_time(arretSort, array)
