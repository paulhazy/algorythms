arr = [4, 7, 5, 6, 1, 3, 5, 9]

def buble_sort(arr):
  for i in range(0, len(arr)-1):
      for j in range(0, len(arr)-1-i):
          if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]

  return arr

print(buble_sort(arr))