# Time
# O(1) best
# O(log n) avg/ worst
# Space
# O(1)

def search(arr, left, right, target):

  if right >= left:
    mid = left + (right - left) // 2
    if arr[mid] == target:
      return mid
    if arr[mid] > target:
      return search(arr, left, mid - 1, target)
    else:
      return search(arr, mid + 1, right, target )
  else:
    return -1



l = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 38
res = search(l, 0, len(l), target)

print("the index is: " + str(res))

# output = the index is: 6

