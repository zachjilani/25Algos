# cant say I really like this one tbh

def counting(arr):
  size = len(arr)
  out = [0] * size

  count = [0] * 10

  for i in range(0, size):
    count[arr[i]] += 1
  for i in range(1, 10):
    count[i] += count[i - 1]
  i = size - 1
  while i >= 0:
    out[count[arr[i]] - 1] = arr[i]
    count[arr[i]] -= 1
    i -= 1
  for i in range(0, size):
    arr[i] = out[i]
  return out

l = [4,2,2,5,7,8,9,0,3]

print(counting(l))

# output = [0, 2, 2, 3, 4, 5, 7, 8, 9]