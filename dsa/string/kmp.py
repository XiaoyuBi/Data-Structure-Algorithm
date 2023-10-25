
def LPS(pattern: str) -> list[int]:
    """
    Longest Prefix Suffix

    lps[0] = 0
    lps[i] = longest prefix in pattern[0..i] which is also 
             the suffix of pattern[0..i] (EXCEPT the whole pattern[0..i])
             Therefore, we always have 0 <= lps[i] <= i
    """
    m = len(pattern)
    lps = [0] * m 

    prev, cur = 0, 1
    while cur < m:
        # if match
        if pattern[prev] == pattern[cur]:
            lps[cur] = lps[prev] + 1
            prev += 1
            cur += 1
        # if not match
        elif prev > 0:
            prev = lps[prev - 1]
        # if not match and prev is as the start
        else: # prev == 0
            lps[cur] = 0
            cur += 1
    
    return lps 

def KMP(search: str, pattern: str) -> int:
    """
    Knuth-Morris-Pratt Algorithm 
    Find the Index of the First Occurrence in a String
    """
    lps = LPS(pattern)
    i, j = 0, 0
    while i < len(search):
        # if match
        if search[i] == pattern[j]:
            i += 1
            j += 1
        # if not match
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1
        
        # end condition, already find the first match index
        if j == len(pattern):
            return i - j
    
    return -1


if __name__ == "__main__":
    search = "AAAXAAAA"

    print(f"Search string {search}")
    print(f"Index for 'AAAA': {KMP(search, 'AAAA')}")
    print(f"Index for 'AAXX': {KMP(search, 'AAXX')}")
