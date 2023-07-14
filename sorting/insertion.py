# Time
# O(n^2)
# Space
# O(1)

def selection(arr):
  for i in range(1, len(arr)):
    j = i - 1
    k = arr[i]
    while j >= 0 and k < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = k
  return arr

arr = [12,11,13,6,5]


print(selection(arr))

output = [5, 6, 11, 12, 13]
