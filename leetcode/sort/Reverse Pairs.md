# Special Usage of Merge Sort

## 493. Reverse Pairs

Given an integer array `nums`, return the __number of reverse pairs__ in the array.

A reverse pair is a pair `(i, j)` where:

- `0 <= i < j < nums.length` and
- `nums[i] > 2 * nums[j]`

Example 1:

```text
Input: nums = [1,3,2,3,1]

Output: 2

Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
```

Example 2:

```text
Input: nums = [2,4,3,5,1]

Output: 3

Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1
```

## Solution

It's straightforward to come up with the $O(n^2)$ method, but we could utilize the merge sort algorithm for a better solution with time complexity $O(n logn)$.

Basically the point here is that within a __sorted__ array, if `nums[i]` is twice as some value, then all numbers right to `nums[i]` are at least twice as some value as well. Therefore, we don't have to go through the whole `nums` array.

```python
from collections import deque

class Solution:

    res = 0

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        m, n = len(left), len(right)
        merged = []

        # general merging sort algorithm
        i, j = 0, 0
        while i < m and j < n:
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        while i < m:
            merged.append(left[i])
            i += 1
        while j < n:
            merged.append(right[j])
            j += 1
        
        # special handling
        i, j = 0, 0
        while i < m and j < n:
            if left[i] > 2 * right[j]:
                self.res += m - i
                j += 1 # IMPORTANT: DO NOT update i here
            else:
                i += 1
        
        return merged
    
    def merge_sort(self, nums: List[int], start: int, end: int):
        if start == end:
            return [nums[start]]
        
        mid = (start + end) // 2
        left = self.merge_sort(nums, start, mid)
        right = self.merge_sort(nums, mid+1, end)
        return self.merge(left, right)

    def reversePairs(self, nums: List[int]) -> int:
        
        merged = self.merge_sort(nums, 0, len(nums) - 1)
        #print(merged)

        return self.res
```
