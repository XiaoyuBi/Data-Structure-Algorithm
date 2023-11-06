# Segment Tree

## 2926. Maximum Balanced Subsequence Sum

You are given a __0-indexed__ integer array nums.

A __subsequence__ of nums having length `k` and consisting of indices $i_0 < i_1 < ... < i_{k-1}$ is __balanced__ if the following holds:

- $nums[i_j] - nums[i_{j-1}] >= i_j - i_{j-1}$, for every `j` in the range `[1, k - 1]`.

A subsequence of nums having length 1 is considered balanced.

Return an integer denoting the __maximum__ possible sum of elements in a __balanced subsequence__ of nums.

A subsequence of an array is a new non-empty array that is formed from the original array by deleting some (possibly none) of the elements without disturbing the relative positions of the remaining elements.

Example 1:

```text
Input: nums = [3,3,5,6]

Output: 14

Explanation: In this example, the subsequence [3,5,6] consisting of indices 0, 2, and 3 can be selected.
nums[2] - nums[0] >= 2 - 0.
nums[3] - nums[2] >= 3 - 2.
Hence, it is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
The subsequence consisting of indices 1, 2, and 3 is also valid.
It can be shown that it is not possible to get a balanced subsequence with a sum greater than 14.
```

Example 2:

```text
Input: nums = [5,-1,-3,8]

Output: 13

Explanation: In this example, the subsequence [5,8] consisting of indices 0 and 3 can be selected.
```

Example 3:

```text
Input: nums = [-2,-1]

Output: -1

Explanation: In this example, the subsequence [-1] can be selected.
```

## Solution

First, we transform the inequity into $nums[i_j] - i_j >= nums[i_{j-1}] - i_{j-1}$

We could then give a straightforward __dynamic programming__ solution, where we denote `dp[i]` as the maximum balanced subsequence sum with `nums[i]` as the last element. During each iteration, we need to check all previous indices $k$ if $nums[k] - k <= nums[i] - i$ and get the largest `dp[k]`. Since checking all previous $k$ will take $O(n)$ time, the total time complexity for this method is $O(n^2)$.

To improve on this, we should try to improve the efficiency on getting previous largest sum. Instead of updating `dp` from `dp[0]` to `dp[n - 1]`, we can initialize `dp` with `-inf` and update `dp[i]` based on the order of `nums[i] - i`. In this way, we do not need to check the inequity at all!

Then, how do we get the previous largest sum? We could use __Segment Tree__ to do range query, and the time complexity will be $O(nlogn)$.

```python
class SegmentTree:
    """
    1-index segment tree
    """
    def __init__(self, n):
        self.n = n
        self.tree = [float("-inf")] * 2 * n
    
    def update(self, idx, value):
        idx += self.n
        self.tree[idx] = value

        while idx > 0:
            self.tree[idx>>1] = max(self.tree[idx], self.tree[idx^1])
            idx >>= 1
    
    def query(self, a, b):
        res = float("-inf")
        a += self.n
        b += self.n

        while a <= b:
            if (a & 1):
                res = max(res, self.tree[a])
                a += 1
            
            if ((b + 1) & 1):
                res = max(res, self.tree[b])
                b -= 1
            
            a >>= 1
            b >>= 1
        
        return res

def maxBalancedSubsequenceSum(nums: List[int]) -> int:
    n = len(nums)
    new_idx = sorted(range(n), key = lambda x: nums[x] - x)

    st = SegmentTree(n)
    for idx in new_idx:
        max_prev_res = st.query(0, idx - 1)
        cur_res = nums[idx] + max(0, max_prev_res)

        st.update(idx, cur_res)
    
    return st.query(0, n - 1)
```
