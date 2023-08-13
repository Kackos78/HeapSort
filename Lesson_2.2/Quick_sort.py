#  Быстрая сортировка
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = list(filter(lambda x: x < pivot, lst))
    center = [i for i in lst if i == pivot]
    right = list(filter(lambda x: x > pivot, lst))
    return quick_sort(left) + center + quick_sort(right)
