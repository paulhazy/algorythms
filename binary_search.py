
def binary_search(seq, item):
# задаём границы списка
    low = 0
    high = len(seq) - 1

    while low <= high:
        mid = low + (high - low) // 2 # если нечётное значение то округляем в меньшую
        mid_val = seq[mid]

        if mid_val == item:
            return mid
        elif item < mid_val:
            high = mid - 1
        else:
            low = mid + 1
    return None
#test
#print(binary_search([2,3,4,6,7,8,9,11], 6))