



"""""
Majority element is defined as an element that
appears more than n/2 times, where n is the
length of the array. Here it is done using
collections library as well as a map.
"""

import collections

def majority_collections(arr):
  length = len(arr)/2
  common = collections.Counter(arr).most_common()[0][1]
  if common > length:
    return collections.Counter(arr).most_common()[0][0]
  return "none"

def majority(arr):
  m = {}
  for i in range(len(arr)):
    if arr[i] in m:
      m[arr[i]] += 1
    else:
      m[arr[i]] = 1
  for key in m:
    if m[key] > len(arr)/2:
      return key


arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]

print(majority_collections(arr))
print()
print(majority(arr))

"""
output for each is 4

"""
