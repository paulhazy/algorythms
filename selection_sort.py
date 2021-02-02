#делаем сортировку выбором
def selection_sort(lst):
    index_len = range(0, len(lst) - 1)
    for i in index_len:
        min_val = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_val]:
                min_val = j
        if min_val != i:
            lst[min_val], lst[i] = lst[i], lst[min_val]
    return lst
#test
#print(selection_sort([45,9,33,1,6,8,3,5]))