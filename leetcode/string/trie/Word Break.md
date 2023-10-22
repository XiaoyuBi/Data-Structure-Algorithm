# Trie Structure

## 140. Word Break II

Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in _any order_.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

```text
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]

Output: ["cats and dog","cat sand dog"]
```

Example 2:

```text
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]

Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

Explanation: Note that you are allowed to reuse a dictionary word.
```

Example 3:

```text
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]

Output: []
```

## Solution

To check if a substring in `s` matches with a word in `wordDict`, generally it will take O(mn) time, for `wordDict` with length `m` and average string length `n`. However, using the _Trie_ data structure, it will reduce a single check to O(n) time. (see [code examples](/dsa/string/trie.py))

Besides the string matching sub-problem, this is a standard __DFS__ problem to get all possible combinations.

```python
class TrieNode:
    def __init__(self, c):
        self.c = c
        self.isEnd = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        
        cur.isEnd = True
    
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.isEnd

def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    myTrie = Trie()
    for word in wordDict:
        myTrie.insert(word)
    
    res = []
    n = len(s)
    def dfs(idx: int, track: str):
        if idx >= n: # only idx == n could be reached
            res.append(track)
            return
        
        for j in range(idx, n):
            sub_str = s[idx: j + 1]
            if myTrie.search(sub_str):
                dfs(j + 1, track + " " + sub_str)
    
    dfs(0, "")
    res = [s[1:] for s in res] # remove starting space
    return res
```
