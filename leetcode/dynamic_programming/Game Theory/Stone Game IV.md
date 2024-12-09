# Game Theory

## 1510. Stone Game IV

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

Example 1:

```text
Input: n = 1

Output: true

Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
```

Example 2:

```text
Input: n = 2

Output: false

Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
```

Example 3:

```text
Input: n = 4

Output: true

Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
```

## Solution

According to [Zermelo's theorem](https://en.wikipedia.org/wiki/Zermelo%27s_theorem_(game_theory)), given `n` stones, either Alice has a must-win strategy, or Bob has one. In game theory, Zermelo's theorem is a theorem about finite two-person games of perfect information in which the players move alternately and in which chance does not affect the decision making process. It says that if the game cannot end in a draw, then one of the two players must have a winning strategy (i.e. can force a win).

Therefore, we can define our `DP` array to represent whether the current player must win at a given state, which is the best outcome of all future states after current player takes an action. Since there are only `n` stones, there will be `n` states and up to $\sqrt n$ actions at a given state, making the total time complexity $O(n \sqrt n)$.

Note: It could speed up more than 10x if we iterate actions from $\sqrt n$ to $1$ instead of from $1$ to $\sqrt n$.

> If we go from $1$ to $\sqrt n$, the recursive call will go as: `winnerSquareGame(n)`, then `winnerSquareGame(n-1)`, which in turn calls `winnerSquareGame(n-2)` etc; meaning we will always get the worst case.
\
> If reversed, `winnerSquareGame(n)` may call `winnerSquareGame(<small_number>)`, which, if returns `False`, means that `winnerSquareGame(n)` will return `True` immediately (without checking other actions).

```python
def winnerSquareGame(n: int) -> bool:
    # x: remaining stones
    @cache
    def dfs(x):
        if x == 0:
            return False
        
        k_max = int(math.sqrt(x))
        return any(not dfs(x - k * k) for k in range(k_max, 0, -1))
    
    return dfs(n)
```
