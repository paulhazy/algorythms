from random import randint
# подключаем модуль для нахождения точки опоры
def quicksort(arr):
    if len(arr) <= 1: # если массив таков нечего нам с ним делать
        return arr
    low, mid, high = [], [], []
    pivot = arr[randint(0, len(arr) - 1)] # находим опорную точку
    for i in arr:           # проходим по каждому элементу в указанном массиве
        if i < pivot:       # если же элемент меньше точки опоры кидаем его на дно
            low.append(i)
        elif i == pivot:    # если элемент равен точке опоры то
            mid.append(i)   # пойдет в середняк
        elif i > pivot:     # если выше опоры то в массив выше
            high.append(i)
    return quicksort(low) + mid + quicksort(high) # итого собираем наши списки воедино и получаем отсортированный массив
#test
#print(quicksort([14,6,7,8,94,3,5,2]))