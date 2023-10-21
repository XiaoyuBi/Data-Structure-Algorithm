
class TrieNode:
    def __init__(self, c: str):
        self.data = c # single character
        self.isEnd = False
        self.children = {} 

class Trie:
    """
    A trie is a rooted tree that maintains a set of strings. 
    Each string in the set is stored as a chain of characters that starts at the root. 
    If two strings have a common prefix, they also have a common chain in the tree.
    """
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word: str):
        cur = self.root
        for c in word:
            if not c in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        
        cur.isEnd = True
    
    def delete(self, word: str):
        if not self.search(word):
            raise ValueError(f"{word} is not found in Trie!")
        
        cur = self.root
        for c in word:
            if not c in cur.children:
                return
            cur = cur.children[c]
        
        cur.isEnd = False
    
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if not c in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.isEnd
    
    def searchStartWith(self, pattern: str) -> list[str]:
        res = []
        cur = self.root
        for c in pattern:
            if not c in cur.children:
                return res 
            cur = cur.children[c]
        
        # from current node, get all nodes with isEnd is true
        def dfs(tmp, prefix):
            if tmp.isEnd:
                res.append(prefix)
            
            for child in tmp.children.values():
                dfs(child, prefix + child.data)
        
        dfs(cur, pattern)
        return res
    

if __name__ == "__main__":
    candidates = set(["canel", "cancel", "the", "there"])

    print(f"Candidates: {candidates}")
    myTrie = Trie()
    for candidate in candidates:
        myTrie.insert(candidate)
    
    print(f"All candidates in trie: {myTrie.searchStartWith('')}")
    print(f"All candidates start with 'the': {myTrie.searchStartWith('the')}")
    print(f"All candidates start with 'canc': {myTrie.searchStartWith('canc')}")

    print(f"Word 'the' in the Trie: {myTrie.search('the')}")
    print("Delete word 'the' for the Trie.")
    myTrie.delete("the")
    print(f"Word 'the' in the Trie: {myTrie.search('the')}")
    print(f"All candidates start with 'the': {myTrie.searchStartWith('the')}")