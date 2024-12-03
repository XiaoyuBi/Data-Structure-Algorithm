# 975. Odd Even Jump

You are given an integer array `arr`. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index `i` to index `j` (with `i < j`) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index `j` such that `arr[i] <= arr[j]` and `arr[j]` is the smallest possible value. If there are multiple such indices `j`, you can only jump to the smallest such index `j`.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index `j` such that `arr[i] >= arr[j]` and `arr[j]` is the largest possible value. If there are multiple such indices `j`, you can only jump to the smallest such index `j`.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index `arr.length - 1`) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

## Solution

This could be rather simply solved with `SortedDict` data structure from package `sortedcontainers`, but let's work it out with just simple Python list (`stack`).

Using dynamic programming, we can define `dp[i] = [bool, bool]` where stands for whether you can start at index `i` with odd/even jumps to get the end. Following this definition, we have `dp[n-1] = [True, True]`, then we want to traverse the array in reverse order.

But how do we know if we can jump from `i` to `j`? We can use the monotonic stack from sorting the whole array together with their indices.

```python
def oddEvenJumps(arr: List[int]) -> int:
    n = len(arr)
    dp = [[0, 0] for _ in range(n)]
    dp[n-1] = [1, 1]

    num_idx = [(num, idx) for idx, num in enumerate(arr)]

    stack = []
    next_higher = [-1] * n
    for num, idx in sorted(num_idx, key = lambda x: (x[0], x[1])):
        while stack and stack[-1] < idx: # i < j
            next_higher[stack.pop()] = idx
        stack.append(idx)

    stack = []
    next_lower = [-1] * n
    for num, idx in sorted(num_idx, key = lambda x: (-x[0], x[1])):
        while stack and stack[-1] < idx:
            next_lower[stack.pop()] = idx
        stack.append(idx)
    
    for i in range(n - 2, -1, -1):
        if next_higher[i] > i:
            dp[i][0] = dp[next_higher[i]][1]
        if next_lower[i] > i:
            dp[i][1] = dp[next_lower[i]][0]
    
    return sum([x for x, _ in dp])
```
