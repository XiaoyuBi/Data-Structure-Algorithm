import timeit
import random
from typing import List

# for reproductivity
NUM_LENGTH = 2_000
random.seed(1998)

# Bubble Sort: O(n^2)
def bubble_sort(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums

# Insertion Sort: O(n^2)
def insertion_sort(nums: List[int]) -> List[int]:
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j] = nums[j + 1]
            j -= 1
        
        nums[j + 1] = key
    
    return nums

# Quick Sort: O(n*log(n))
def quick_sort(nums: List[int], low = None, high = None) -> List[int]:
    n = len(nums)
    if not low: low = 0
    if not high: high = n - 1
    if low >= high: return 

    pi = partition(nums, low, high)
    quick_sort(nums, low, pi - 1)
    quick_sort(nums, pi + 1, high)
    return nums
## helper
def partition(nums: List[int], low, high) -> None:
    if low >= high: return 
    
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1

# Merge Sort: O(n*log(n))
def merge_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    if n <= 1:
        return nums
    
    left = merge_sort(nums[: n // 2])
    right = merge_sort(nums[n // 2:])
    return merge(left, right)
def natural_merge_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    if n <= 1:
        return nums
    
    runs = []
    l, r = 0, 1
    while r < n:
        if nums[r] < nums[r - 1]:
            runs.append(nums[l: r])
            l = r 
        r += 1
    runs.append(nums[l: r]) # the final run

    while len(runs) > 1:
        i = 0
        new_runs = []
        while i < len(runs) - 1:
            new_runs.append(merge(runs[i], runs[i + 1]))
            i += 2
        
        if i < len(runs):
            new_runs.append(runs[i])
        
        runs = new_runs 
    
    return runs[0]
## helper
def merge(left, right):
    l, r = 0, 0
    res = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    
    res.extend(left[l:])
    res.extend(right[r:])
    
    return res

# Tim Sort: Insertion + Merge Sort
# can be seen as natural merge sort with fixed step size
def tim_sort(nums: List[int]) -> List[int]:
    MIN_MERGE = 32
    n = len(nums)

    runs = []
    for i in range(0, n, MIN_MERGE):
        j = min(i + MIN_MERGE, n)
        runs.append(insertion_sort(nums[i: j]))
    
    while len(runs) > 1:
        i = 0
        new_runs = []
        while i < len(runs) - 1:
            new_runs.append(merge(runs[i], runs[i + 1]))
            i += 2
        
        if i < len(runs):
            new_runs.append(runs[i])
        
        runs = new_runs 
    
    return runs[0]

# Count Sort: O(n) + space O(C)
def count_sort(nums: List[int]) -> List[int]:
    res = []
    counts = [0] * (NUM_LENGTH + 1)
    for num in nums:
        counts[num] += 1
    
    for i, count in enumerate(counts):
        res.extend([i] * count)
    
    return res


def test_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"
    time = timeit.timeit(stmt=stmt, setup=setup_code, number=10)

    print(f"Algorithm: {algorithm:12s} \t Execution time: {time:.6f}")


if __name__ == "__main__":
    nums = [random.randint(0, NUM_LENGTH) for _ in range(NUM_LENGTH)]
    print(f"Testing array has length {NUM_LENGTH} within range (0, {NUM_LENGTH})")

    # Bubble Sort
    test_sorting_algorithm("bubble_sort", nums)
    # Insertion Sort
    test_sorting_algorithm("insertion_sort", nums)
    # Quick Sort
    test_sorting_algorithm("quick_sort", nums)
    # Merge Sort
    test_sorting_algorithm("merge_sort", nums)
    # Natural Merge Sort
    test_sorting_algorithm("natural_merge_sort", nums)
    # Tim Sort
    test_sorting_algorithm("tim_sort", nums)
    # Count Sort
    test_sorting_algorithm("count_sort", nums)
    # Built-in Sort
    test_sorting_algorithm("sorted", nums)
    