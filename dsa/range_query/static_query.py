import math

class PrefixSum:

    preSum: list[int] = []

    def __init__(self, nums: list[int]):
        self.nums = nums 
        self.__prefix_sum()

    # query in O(1)
    def query_sum(self, a: int, b: int) -> int:
        if a > b or a < 0:
            raise ValueError("Range is not valid!")
        
        if a == 0:
            return self.preSum[b]
        elif a > 0:
            return self.preSum[b] - self.preSum[a - 1]
    
    # build in O(n)
    def __prefix_sum(self) -> list[int]:
        if not self.nums: 
            return
        
        self.preSum = [self.nums[0]]
        for num in self.nums[1:]:
            self.preSum.append(self.preSum[-1] + num)


class SparseTable:
    """
    The idea is to precalculate all values of argmin_q(a,b) 
    where b-a+1 (the length of the range) is a power of two.
    """

    sparse_table: list[list[int]] # [i][j] stands for argmin in range [i, i + 2^j - 1]

    def __init__(self, nums: list[int]):
        self.nums = nums 
        self.__build_table()
    
    # query in O(1)
    def query_argmin(self, a: int, b: int) -> int:
        if a > b or a < 0:
            raise ValueError("Range is not valid!")
        
        # Let j be the largest power of two that does not exceed b−a+1
        # Check [a, a + k - 1] and [b - k + 1, b]
        j = int(math.log2(b - a + 1))

        c1 = self.sparse_table[a][j]
        c2 = self.sparse_table[b - (1 << j) + 1][j]
        c = c1 
        if self.nums[c2] < self.nums[c1]:
            c = c2 
        
        return c
    
    # build in O(n*log(n)), with extra space in O(n*log(n))
    # There are also more sophisticated techniques where the preprocessing time is only O(n)
    # https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=340fde0d3787e07c2ff02a8e323c33eb6cbef620
    def __build_table(self):
        n = len(self.nums)
        log_n = int(math.log2(n)) + 1
        self.sparse_table = [[0] * log_n for _ in range(n)]
        
        # special: range length: 1
        for i in range(n):
            self.sparse_table[i][0] = i
        
        # range length: 2^j == 1 << j
        j = 1
        while (1 << j) <= n:
            i = 0
            while i + (1 << j) - 1 < n:
                # two candidates
                c1 = self.sparse_table[i][j - 1]
                c2 = self.sparse_table[i + (1 << (j - 1))][j - 1]
                c = c1
                if self.nums[c2] < self.nums[c1]:
                    c = c2
                self.sparse_table[i][j] = c

                i += 1
            j += 1


if __name__ == "__main__":
    nums = [1, 3, 4, 8, 6, 1, 4, -2, 1]
    myPrefixSum = PrefixSum(nums)
    mySparseTable = SparseTable(nums)
    
    print(f"Orignal nums: {nums}")

    print("Prefix Sum Algorithm:")
    # print(f"Prefix Sum: {myPrefixSum.preSum}")
    print(f"Range [0, 1] sum: {myPrefixSum.query_sum(0, 1)}")
    print(f"Range [0, 5] sum: {myPrefixSum.query_sum(0, 5)}")
    print(f"Range [6, 7] sum: {myPrefixSum.query_sum(6, 7)}")

    print("Sparse Table Algorithm:")
    # print(f"Sparse Table: {mySparseTable.sparse_table}")
    print(f"Range [1, 6] argmin: {mySparseTable.query_argmin(1, 6)}")
    print(f"Range [0, 4] argmin: {mySparseTable.query_argmin(0, 4)}")
    print(f"Range [3, 7] argmin: {mySparseTable.query_argmin(3, 7)}")
