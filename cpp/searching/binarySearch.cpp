#include <iostream>
#include <cmath>
using namespace std;

int binarySearch(int arr[], int left, int right, int target)
{
  int mid;
  if (right >= left)
  {
    mid = floor(left + (right - left) / 2);
    if (arr[mid] == target)
    {
      return mid;
    }
    if (arr[mid] > target)
    {
      return binarySearch(arr, left, mid - 1, target);
    }
    else
    {
      return binarySearch(arr, mid + 1, right, target);
    }
  }
  else
  {
    return -1;
  }
}

int main()
{
  int l[10] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
  int size = 10;
  int target = 38;
  int res = binarySearch(l, 0, 10, target);

  if (res == -1)
  {
    cout << "number not found" << endl;
  }
  else
  {
    cout << res << endl;
  }
}