# Time
# O(nlog n)
# Space
# O(n)

def merge(arr):

  #len of 1 has nothing left to split: base case
  if len(arr) > 1:

    #find midpoint of array
    mid = len(arr) // 2

    #separate into two sides at mid point
    left = arr[:mid]
    right = arr[mid:]

    #recursively separate into two sides until base case
    merge(left)
    merge(right)

    #indices for the left and right temp arrays, and original array
    i = j = k = 0

    #while there are still indices in left and right array
    while i < len(left) and j < len(right):

      #if left array value is less than right array at same value,
      # then that value goes into the origianl arr
      if left[i] <= right[j]:
        arr[k] = left[i]

        #increment index for i or left array
        i += 1

      #if left array value is more, then the right array value
      #goes into the original arr. however we still need to
      #compare left[i] value with others to find its place.
      #that is why we need to use j here
      else:
        arr[k] = right[j]

        #increment index for j or right array
        j += 1

      #increment index for k or original array
      k += 1

    #checking for any leftover
    while i < len(left):
      arr[k] = left[i]
      i += 1
      k += 1
    while j < len(right):
      arr[k] = right[j]
      j += 1
      k += 1

  return arr

arr = [38, 27, 43, 3, 9, 82, 10]

print(merge(arr))

# output = [3, 9, 10, 27, 38, 43, 82]
