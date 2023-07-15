

def partition(arr, low, high):
  pivot = arr[high]

  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i],arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def quick(arr, low, high):
  if low < high:
    p = partition(arr, low, high)

    quick(arr, low, p - 1)
    quick(arr, p + 1, high)
  return arr

arr = [10, 7, 8, 9, 1, 5, 25, 4, 6, 11]

print(quick(arr, 0, (len(arr) - 1)))


