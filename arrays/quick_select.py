

def partition(arr, l, r):
  x = arr[r]
  i = l
  for j in range(i, r):
    if arr[j] <= x:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
  arr[i], arr[r] = arr[r], arr[i]
  return i

def ksmallest(arr, l, r, k):
  if k > 0 and k <= r - l + 1:
    index = partition(arr, l, r)
    if(index - 1 == k - 1):
      return arr[index]
    if(index - 1 > k - 1):
      return ksmallest(arr, l, index - 1, k)
    return ksmallest(arr, index + 1, r, k - index + l - 1)
  print("not in bounds of array")