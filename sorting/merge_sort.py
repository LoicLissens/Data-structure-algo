from typing import List
from math import floor

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = floor(len(arr) / 2)
    left = arr[:mid]
    right = arr[mid:]
    leftSorted = merge_sort(left)
    rightSorted = merge_sort(right)
    return merge(leftSorted, rightSorted)

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    assert sorted_arr == [11, 12, 22, 25, 34, 64, 90], f"Expected [11, 12, 22, 25, 34, 64, 90], but got {sorted_arr}"