# Dynamic Programming

## 1755. Closest Subsequence Sum

You are given an integer array `nums` and an integer `goal`.

You want to choose a subsequence of `nums` such that the sum of its elements is the closest possible to `goal`. That is, if the sum of the subsequence's elements is `sum`, then you want to minimize the absolute difference `abs(sum - goal)`.

Return the _**minimum**_ possible value of `abs(sum - goal)`.

Note that a subsequence of an array is an array formed by removing some elements (**possibly all or none**) of the original array.

Example 1:

```text
Input: nums = [5,-7,3,5], goal = 6

Output: 0

Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.
```

Example 2:

```text
Input: nums = [7,-9,15,-2], goal = -5

Output: 1

Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
```

Example 3:

```text
Input: nums = [1,2,3], goal = -7

Output: 7
```

Constraints:

- `1 <= nums.length <= 40`

## Solution

Hint1: The naive solution is to check all possible subsequences. This works in $O(2^n)$.

Hint2: Divide the array into two parts of nearly is equal size.

Hint3: Consider all subsets of one part and make a list of all possible subset sums and sort this list.

Hint4: Consider all subsets of the other part, and for each one, let its sum = x, do binary search to get the nearest possible value to goal - x in the first part.

```python
# Stupid method to get all subsequence sums :(
def getSums(nums):
    nums_sums = []
    def dfs(s, idx):
        if idx == len(nums):
            nums_sums.append(s)
            return
        
        dfs(s, idx + 1)
        dfs(s + nums[idx], idx + 1)
    
    dfs(0, 0)
    return nums_sums

# Elegant method to get all subsequence sums :)
def getSums_(nums):
    nums_sums = {0}
    for num in nums:
        nums_sums |= {num + x for x in nums_sums}
    
    return list(nums_sums)

def binary_search(nums, target):
    # return: maximum idx s.t. nums[idx] <= target
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    
    return r

def minAbsDifference(nums: List[int], goal: int) -> int:
    n = len(nums)
    arr1 = nums[:n // 2]
    arr2 = nums[n // 2:]

    arr1_sums = self.getSums_(arr1)
    arr2_sums = self.getSums_(arr2)
    arr1_sums.sort()
    arr2_sums.sort()

    res = float("inf")
    l, r = 0, len(arr2_sums) - 1
    while l < len(arr1_sums) and r >= 0:
        val = arr1_sums[l] + arr2_sums[r]
        if val == goal:
            return 0
        
        res = min(res, abs(val - goal))
        if val > goal:
            r -= 1
        else:
            l += 1
    
    return res
```
