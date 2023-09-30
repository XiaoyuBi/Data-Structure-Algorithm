
# Recursive Building for sum query
class SegmentTreeNode:

    def __init__(self, start: int, end: int, sum: int,
                left: 'SegmentTreeNode' = None, 
                right: 'SegmentTreeNode' = None):
        self.start = start
        self.end = end 
        self.sum = sum 

        self.left = left 
        self.right = right

class SegmentTree:

    tree: SegmentTreeNode
    
    def __init__(self, nums: list[int]):
        self.nums = nums 
        self.tree = self.__build_tree(0, len(nums) - 1)

    # query in O(log(n))
    def query_sum(self, a: int, b: int, root: SegmentTreeNode = None) -> int:
        if root == None:
            root =  self.tree
        
        if root.start == a and root.end == b:
            return root.sum
        
        mid = (root.start + root.end) // 2
        if b <= mid:
            return self.query_sum(a, b, root.left)
        elif a > mid:
            return self.query_sum(a, b, root.right)
        else:
            return self.query_sum(a, mid, root.left) + \
                   self.query_sum(mid + 1, b, root.right)
    
    # update in O(log(n))
    def update(self, idx: int, val: int, root: SegmentTreeNode = None):
        if root == None:
            root = self.tree
        # update root value
        root.sum += val 
        # find the leaf node, stop searching
        if root.start == root.end == idx:
            return 
        
        mid = (root.start + root.end) // 2
        if idx <= mid:
            self.update(idx, val, root.left)
        else:
            self.update(idx, val, root.right)

    def __build_tree(self, start: int, end: int) -> SegmentTreeNode:
        if start == end:
            return SegmentTreeNode(start, end, self.nums[start])
        
        mid = (start + end) // 2
        left = self.__build_tree(start, mid)
        right = self.__build_tree(mid + 1, end)
        return SegmentTreeNode(start, end, left.sum + right.sum, left, right)


if __name__ == "__main__":
    nums = [1, 3, 4, 8, 6, 1, 4, 2]
    mySegTree = SegmentTree(nums)
    
    print(f"Orignal nums: {nums}")

    print("Segment Tree:")
    print(f"Range [0, 1] sum: {mySegTree.query_sum(0, 1)}")
    print(f"Range [0, 6] sum: {mySegTree.query_sum(0, 6)}")
    print(f"Range [6, 7] sum: {mySegTree.query_sum(6, 7)}")

    print(f"Update index 3 with -4")
    mySegTree.update(3, -4)
    print(f"Range [1, 3] sum: {mySegTree.query_sum(1, 3)}")