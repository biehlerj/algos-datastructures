from math import floor, sqrt


def jump_search(arr: list[int], arr_len: int, target: int) -> int:
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
        A number representing the index of the target
    """
    lower = 0
    jump = floor(sqrt(arr_len))

    while arr[min(jump, arr_len) - 1] < target:
        lower = jump
        jump += jump
        if lower >= arr_len:
            return -1

    while arr[lower] < target:
        lower += 1
        if lower == min(jump, arr_len):
            return -1

    if arr[lower] == target:
        return lower
    return -1
