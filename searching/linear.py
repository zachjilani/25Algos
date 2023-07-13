# Time
# O(n)
# Space
# O(1)

def search(arr, value):

  for i in arr:
    if arr[i] == value:
      return i
  return -1

l = [1,2,3,4,5,6,7]

val = 4

res = search(l, val)

print("the index is: " + str(res))

# output = the index is: 3