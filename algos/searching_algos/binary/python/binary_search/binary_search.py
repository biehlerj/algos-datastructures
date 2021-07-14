from math import floor


def binary_search(arr: list[int], arr_len: int, target: int) -> int:
    """Finds the target value in an array of arr_len

    Parameters
    ----------
    arr : list[int]
        The array to search
    arr_len : int
        The length of the array
    target : int
        The number to find in the array

    Returns
    -------
    int
        A number representing the index of target
    """
    left = 0
    right = arr_len - 1

    while left <= right:
        middle = floor((left + right) / 2)

        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1
        else:
            return middle
    return -1
