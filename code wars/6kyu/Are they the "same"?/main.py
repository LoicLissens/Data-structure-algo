def comp(array1: list[int], array2: list[int]) -> bool:
    if array1 is None or array2 is None:
        return False
    return sorted([i**2 for i in array1]) == sorted(array2)