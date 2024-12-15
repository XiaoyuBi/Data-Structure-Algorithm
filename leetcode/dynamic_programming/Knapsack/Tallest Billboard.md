# Knapsack

## 956. Tallest Billboard

You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have `rods` of lengths `1`, `2`, and `3`, you can weld them together to make a support of length `6`.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return `0`.

Example 1:

```text
Input: rods = [1,2,3,6]

Output: 6

Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
```

Example 2:

```text
Input: rods = [1,2,3,4,5,6]

Output: 10

Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
```

Example 3:

```text
Input: rods = [1,2]

Output: 0

Explanation: The billboard cannot be supported, so we return 0.
```

Constraints:

- `1 <= rods.length <= 20`
- `1 <= rods[i] <= 1000`
- `sum(rods[i]) <= 5000`

## Solution

A straightforward solution would be exhausting all $3^n$ combinations, which does not fit with the time constraint of this problem. Then, one possible improvement is using a `meet-in-the-middle` technique, which involves breaking the problem into halves and solving them separately. It is because $2 \cdot O(3^\frac{n}{2}) < O(3^n)$, especially when `n` is relatively large.

Then there comes with the issue that how should we store the states. The trivial idea is to use pairs like `(left, right)`, but this will make matching results from two halves hard, could take $O(3^\frac{n}{2}) \cdot O(3^\frac{n}{2}) = O(3^n)$ time. Note that when we do the matching, we only care about the difference between `left` and `right`, therefore a brilliant way to define the states is to set `diff = left - right` and `states[diff] = left`. (`states[diff] = right` could also work, as long as you make sure two halves are using the same side) Also, we want only the largest `left` given the same `diff`, because we want the final summation from two halves to be the largest. With this setup, after we iterate all states from both halves, for each `diff` in the `first_half`, we only need to find `-diff` from the `second_half` (if any) and that will make a valid answer.

```python
def tallestBillboard(rods):
    # Helper function to collect every combination `(left, right)`
    def helper(half_rods):
        states = set()
        states.add((0, 0))
        for r in half_rods:
            new_states = set()
            for left, right in states:
                new_states.add((left + r, right))
                new_states.add((left, right + r))
            states |= new_states
            
        dp = {}
        for left, right in states:
            dp[left - right] = max(dp.get(left - right, 0), left)
        return dp

    n = len(rods)
    first_half = helper(rods[:n // 2])
    second_half = helper(rods[n // 2:])

    answer = 0
    for diff in first_half:
        if -diff in second_half:
            answer = max(answer, first_half[diff] + second_half[-diff])
    return answer
```

A further improvement could be made. Let `n` be the length of the input array `rods` and `m` be the maximum sum of `rods`. This new method will have time complexcity of $O(n \cdot m)$.

```python
def tallestBillboard(rods: List[int]) -> int:
    # dp[taller - shorter] = taller
    dp = {0:0}
    
    for r in rods:
        # dp.copy() means we don't add r to these stands.
        new_dp = dp.copy()
        for diff, taller in dp.items():
            shorter = taller - diff
            
            # Add r to the taller stand, thus the height difference is increased to diff + r.
            new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
            
            # Add r to the shorter stand, the height difference is expressed as abs(shorter + r - taller).
            new_diff = abs(shorter + r - taller)
            new_taller = max(shorter + r, taller)
            new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
            
        dp = new_dp
        
    # Return the maximum height with 0 difference.
    return dp.get(0, 0)
```
