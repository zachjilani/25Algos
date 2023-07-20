
#same partition function found in quick sort
def partition(arr, l, r):
  #pivot point is set to the array end
  x = arr[r]
  #i is set to the low end
  i = l
  #for each index from low to high
  for j in range(i, r):
    #if the array at j is less than the pivor
    if arr[j] <= x:
      #the array at low end and current index swap
      arr[i], arr[j] = arr[j], arr[i]
      #index moves up one
      i += 1
  #after the loop
  arr[i], arr[r] = arr[r], arr[i]
  return i

def ksmallest(arr, l, r, k):
  #making sure k is in the bounds of array
  if k > 0 and k <= r - l + 1:
    index = partition(arr, l, r)
    if(index - 1 == k - 1):
      return arr[index]
    if(index - 1 > k - 1):
      return ksmallest(arr, l, index - 1, k)
    return ksmallest(arr, index + 1, r, k - index + l - 1)
  print("not in bounds of array")