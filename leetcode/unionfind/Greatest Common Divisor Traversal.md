# Union Find

## 2709. Greatest Common Divisor Traversal

You are given a **0-indexed** integer array `nums`, and you are allowed to traverse between its indices. You can traverse between index `i` and index `j`, `i != j`, if and only if `gcd(nums[i], nums[j]) > 1`, where gcd is the greatest common divisor.

Your task is to determine if for **every pair** of indices `i` and `j` in nums, where `i < j`, there exists a sequence of traversals that can take us from `i` to `j`.

Return `true` if it is possible to traverse between all such pairs of indices, or `false` otherwise.

Example 1:

```text
Input: nums = [2,3,6]

Output: true

Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
```

Example 2:

```text
Input: nums = [3,9,5]

Output: false

Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
```

Example 3:

```text
Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
```

## Solution

It is straightfoward to come up with the $O(n^2)$ method, however, we would like to improve on that.

Importantly, we should note that only the prime factors of the `nums` elements matter. (Also worth to note the implementation below of searching for prime factors given an integer.) As long as two elements share a same prime factor, we can do traversal between them, or we can say they are connected in terms of graph.

Our goal is to show whether the graph is fully connected or not. This could be done by DFS, BFS or Union Find.

```python
import math

class UnionFind:
    def __init__(self, n):
        self.links = [i for i in range(n)]
        self.sizes = [1] * n
    
    def find(self, x):
        while self.links[x] != x:
            x = self.links[x]
        
        return x
    
    def get_size(self, x):
        return self.sizes[self.find(x)]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        if self.sizes[x] < self.sizes[y]:
            x, y = y, x
        
        self.links[y] = x
        self.sizes[x] += self.sizes[y]

class Solution:
    def factor(self, num: int) -> List[int]:
        res = []
        MAX_FACTOR = int(math.sqrt(num))

        # prime factor 2
        if num % 2 == 0:
            res.append(2)
        while num % 2 == 0:
            num //= 2
        
        # all other factors must be odd primes
        for p in range(3, MAX_FACTOR + 2, 2):
            if num % p == 0:
                res.append(p)
            while num % p == 0:
                num //= p
        
        # !!! the number itself could be a prime
        if num > 1:
            res.append(num)
        
        return res

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        visited_prime = {}
        myUnion = UnionFind(len(nums))

        for i, num in enumerate(nums):
            for p in self.factor(num):
                if p not in visited_prime:
                    visited_prime[p] = i
                else:
                    myUnion.union(visited_prime[p], i)
        
        return myUnion.get_size(0) == len(nums)
```
