# Сортировка кучей

from random import randint
from time import time

def list_gen(mi=-5, ma=5, le=10):
    return [randint(mi, ma) for i in range(le)]

def HeapSort(list, heapSize, rootIndex):
    largest = int(rootIndex)
    leftChild = int(2 * rootIndex + 1)
    rightChild = int(2 * rootIndex + 2)

    if leftChild < heapSize and list[leftChild] > list[largest]:
        largest = leftChild

    if rightChild < heapSize and list[rightChild] > list[largest]:
        largest = rightChild

    if largest != rootIndex:
        temp = list[int(rootIndex)]
        list[int(rootIndex)] = list[largest]
        list[largest] = temp

        HeapSort(list, heapSize, largest)
    return list


def HeapPreSort(list):
    i = len(list) / 2 - 1
    while i >= 0:
        HeapSort(list, len(list), i)
        i -= 1

    i = len(list) - 1
    while i >= 0:
        list[0], list[i] = list[i], list[0]
        HeapSort(list, i, rootIndex=0)
        i -= 1

    return list




my_list = list_gen()
print(my_list)
my_list_sorted = HeapPreSort(my_list)
print(my_list_sorted)