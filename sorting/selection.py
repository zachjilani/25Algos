# pro: in place
# con: O(n^2) runtime

def selection(arr):
  for step in range(len(arr)):
    min_index = step

    for i in range(step + 1, len(arr)):
      if arr[i] < arr[min_index]:
        min_index = i
    arr[step], arr[min_index] = arr[min_index], arr[step]
  return arr



arr = [20, 12, 10, 15, 2]

print(selection(arr))

# output = [2, 10, 12, 15, 20]