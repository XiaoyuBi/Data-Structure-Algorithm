
class BITree:
    """
    A binary indexed tree or a Fenwick tree can be seen as a dynamic variant of a prefix sum array. 
    It supports two O(logn) time operations on an array: 
    processing a range sum query and updating a value.
    """

    tree : list[int]

    def __init__(self, nums: list[int]):
        self.nums = nums 
        self.__build_tree()
    
    # update in O(log(n))
    def update(self, idx: int, val: int):
        """
        Update Tree: 
        parent_idx = idx + lowbit(idx)
        """
        # update change of value at position idx (0-index)
        idx += 1 # update to comply with 1-index BITree

        while idx < len(self.tree):
            self.tree[idx] += val 
            idx += idx & (-idx) # add last set bit
    
    # query in O(log(n))
    def query_sum(self, a: int, b: int | None = None) -> int:
        """
        Query Tree: 
        parent_idx = idx - lowbit(idx)
        """
        res = 0

        # sum [0..a] (0-index)
        if b == None:
            a += 1
            while a > 0:
                res += self.tree[a]
                a -= a & (-a) # flip last set bit
            
            return res
        # sum [a..b] (0-index)
        else:
            return self.query_sum(b) - self.query_sum(a - 1)

    # build in O(n*log(n)), with extra space in O(n)
    def __build_tree(self):
        n = len(self.nums)
        self.tree = [0] * (n + 1) # Use 1-index for easy implementation

        for i in range(n):
            self.update(i, self.nums[i])


if __name__ == "__main__":
    nums = [1, 3, 4, 8, 6, 1, 4, 2]
    myBITree = BITree(nums)
    
    print(f"Orignal nums: {nums}")

    print("Binary Index Tree:")
    print(f"BITree: {myBITree.tree}")
    print(f"Range [0, 1] sum: {myBITree.query_sum(0, 1)}")
    print(f"Range [0, 6] sum: {myBITree.query_sum(0, 6)}")
    print(f"Range [6, 7] sum: {myBITree.query_sum(6, 7)}")