import random
from typing import List

# for reproductivity
random.seed(1998)

class MyHeap:

    def __init__(self, nums: List[int]):
        self.nodes = []
        self.__heapify(nums)
    
    def push(self, new_value: int):
        self.nodes.append(new_value)
        self.__bubble_up()
    
    def pop(self) -> int:
        """
        Pop lowest element from the heap (usually root). To avoid memory shift
        of first-element removal, we copy the last element to the first
        position, shrink the size by 1 and heapify down.
        """
        if len(self.nodes) == 0:
            raise ValueError("Cannot pop from empty heap!")
        
        last_value = self.nodes.pop()
        if len(self.nodes) == 0: 
            return last_value

        popped_value = self.nodes[0]
        self.nodes[0] = last_value
        self.__bubble_down()
        return popped_value
    
    def __heapify(self, nums: List[int]) -> List[int]:
        for num in nums:
            self.nodes.append(num)
            self.__bubble_up()

    def __bubble_up(self, new_idx: int | None = None):
        if new_idx == None:
            new_idx = len(self.nodes) - 1
        
        parent_idx = self.__get_parent_idx(new_idx)
        if  self.__has_parent(new_idx) and \
            self.nodes[new_idx] < self.nodes[parent_idx]:
            # if new value is smaller than parent, swap the values
            self.nodes[new_idx], self.nodes[parent_idx] = \
            self.nodes[parent_idx], self.nodes[new_idx]

            self.__bubble_up(parent_idx)

    def __bubble_down(self, cur_idx: int | None = 0):
        if not self.__has_left(cur_idx): 
            return 

        # get the smaller one from left and right children
        child_idx = self.__get_left_idx(cur_idx)
        if self.__has_right(cur_idx):
            right_idx = self.__get_right_idx(cur_idx)
            if self.nodes[right_idx] < self.nodes[child_idx]:
                child_idx = right_idx
        
        # if the cur value is greater than child value
        if self.nodes[cur_idx] > self.nodes[child_idx]:
            self.nodes[cur_idx], self.nodes[child_idx] = \
            self.nodes[child_idx], self.nodes[cur_idx]
            self.__bubble_down(child_idx)

    def __len__(self):
        return len(self.nodes)
    
    def __get_left_idx(self, idx: int) -> int:
        return 2 * idx + 1
    def __get_right_idx(self, idx: int) -> int:
        return 2 * idx + 2
    def __get_parent_idx(self, idx: int) -> int:
        return (idx - 1) // 2
    def __has_left(self, idx: int) -> bool:
        return self.__get_left_idx(idx) < len(self.nodes)
    def __has_right(self, idx: int) -> bool:
        return self.__get_right_idx(idx) < len(self.nodes)
    def __has_parent(self, idx: int) -> bool:
        return self.__get_parent_idx(idx) >= 0


if __name__ == "__main__":
    
    nums = [random.randint(0, 10) for _ in range(10)]
    print(f"Orginal: {nums}")
    
    myHeap = MyHeap(nums)
    print(f"Heapified: {myHeap.nodes}")
    myHeap.push(2)
    print(f"Push 2: {myHeap.nodes}")
    myHeap.pop()
    print(f"Pop: {myHeap.nodes}")
    myHeap.push(1)
    print(f"Push 1: {myHeap.nodes}")