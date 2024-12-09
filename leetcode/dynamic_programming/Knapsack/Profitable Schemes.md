# Knapsack

## 879. Profitable Schemes

There is a group of `n` members, and a list of various crimes they could commit. The `ith` crime generates a `profit[i]` and requires `group[i]` members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least `minProfit` profit, and the total number of members participating in that subset of crimes is at most `n`.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo $10^9+7$.

Example 1:

```text
Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]

Output: 2

Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
```

Example 2:

```text
Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]

Output: 7

Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
```

Constraints:

- `1 <= n <= 100`
- `0 <= minProfit <= 100`
- `1 <= group.length <= 100`
- `1 <= group[i] <= 100`
- `profit.length == group.length`
- `0 <= profit[i] <= 100`

## Solution

We denote `minProfit` as $P$ and length of `group` array as $M$, then the initial straightforward idea is to iterate all $2^M$ combination of schemes to see if they fit our requirement of people limit and minimum profit. Obviously this will excess time limit as an exponential solution.

Then we notice the ranges of $N$, $P$ and $M$ are all relatively small, and these 3 paramters are sufficient to represent the whole problem states. That is, if we can count profitable schemes for any given $(n, p, m)$ state, then we can do summation in $O(NPM)$ time to calculate the final answer.

> Note: Here is an important trick to further reduce number of states. Since we do not care about any profits that are already over `minProfit`, we can define the `p` state only taking values from `0` to `minProfit`.

```python
def profitableSchemes(n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    MOD = 10 ** 9 + 7
    m = len(group)

    @cache
    def dfs(people, goal, idx):
        if idx >= m:
            if goal <= 0:
                return 1
            else:
                return 0
        
        res = 0
        # 1. take this job at idx
        if people >= group[idx]:
            new_goal = max(0, goal - profit[idx])
            res += dfs(people - group[idx], new_goal, idx + 1)
        # 2. not take this job
        res += dfs(people, goal, idx + 1)

        return res % MOD
    
    return dfs(n, minProfit, 0)
```

In the above implementation, in fact we still follow the idea of iterating through all $2^M$ combination of schemes, simply with [memoization](https://en.wikipedia.org/wiki/Memoization) of visited states.

Below is an improved implementation with Bottom-Up DP.

```python
def profitableSchemes(n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
    mod = int(1e9) + 7
    dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for k in range(1, len(group) + 1):
        g = group[k - 1]
        p = profit[k - 1]
        for i in range(n, g - 1, -1):
            for j in range(minProfit, -1, -1):
                dp[i][j] = (dp[i][j] + dp[i - g][max(0, j - p)]) % mod
    
    return sum(dp[i][minProfit] for i in range(n + 1)) % mod
```
