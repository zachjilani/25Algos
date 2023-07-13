#  Time
# O(nlog n)
# Space
# O(1)

arr = [4, 10, 3, 5, 1]

def heapify(arr, n, i):
  largest = i
  left = 2*i+1
  right = 2*i+2

  if left < n and arr[largest] < arr[left]:
    largest = left
  if right < n and arr[largest]< arr[right]:
    largest = right
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)

def heap(arr):
  n = len(arr)

  for i in range(n//2 - 1, -1, -1):
    heapify(arr, n, i)
  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
  return arr

print(heap(arr))

# output = [1, 3, 4, 5, 10]