from typing import List


def how_many_swaps(arr: List[int]):
    swaps = 0
    for first_index in range(len(arr)):
        for second_index in range(first_index+1, len(arr)):
            if arr[first_index] > arr[second_index]:
                arr[first_index], arr[second_index] = arr[second_index], arr[first_index]
                swaps = swaps+1
    return swaps


print(how_many_swaps([1, 5, 4, 3, 2]))
print(how_many_swaps([4, 3, 1, 2]))
print(how_many_swaps([5, 1, 4, 2]))
