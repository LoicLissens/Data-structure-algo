from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
   swapped = True
   while swapped:
      for i in range(len(arr) - 1):
         swapped = False
         if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i] # swap n and n + 1
            swapped = True
   return arr

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    assert sorted_arr == [11, 12, 22, 25, 34, 64, 90], f"Expected [11, 12, 22, 25, 34, 64, 90], but got {sorted_arr}"