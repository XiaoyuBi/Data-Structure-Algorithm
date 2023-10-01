import random
from typing import List

# for reproductivity
random.seed(1998)

class MyHeap:

    def __init__(self, nums: List[int]):
        self.nodes = nums[:]
        self.__heapify()
    
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
    
    def __heapify(self):
        n = len(self.nodes)
        for i in range(n // 2, -1, -1):
            self.__bubble_down(i)

    def __bubble_up(self, new_idx: int | None = None):
        if new_idx == None:
            new_idx = len(self.nodes) - 1
        parent_idx = self.__get_parent_idx(new_idx)
        # if new value is smaller than parent
        while parent_idx >= 0 and \
              self.nodes[new_idx] < self.nodes[parent_idx]:
            self.nodes[new_idx], self.nodes[parent_idx] = \
            self.nodes[parent_idx], self.nodes[new_idx]

            new_idx = parent_idx
            parent_idx = self.__get_parent_idx(new_idx)

    def __bubble_down(self, cur_idx: int | None = 0):
        child_idx = self.__get_smaller_child_idx(cur_idx)
        # if the cur value is greater than child value
        while child_idx != None and \
              self.nodes[cur_idx] > self.nodes[child_idx]:
            self.nodes[cur_idx], self.nodes[child_idx] = \
            self.nodes[child_idx], self.nodes[cur_idx]
            
            cur_idx = child_idx
            child_idx = self.__get_smaller_child_idx(cur_idx)

    def __len__(self):
        return len(self.nodes)
    
    def __get_left_idx(self, idx: int) -> int:
        return 2 * idx + 1
    def __get_right_idx(self, idx: int) -> int:
        return 2 * idx + 2
    def __get_parent_idx(self, idx: int) -> int:
        return (idx - 1) // 2
    def __get_smaller_child_idx(self, idx: int) -> int | None:
        if not self.__has_left(idx): 
            return None 
        
        child_idx = self.__get_left_idx(idx)
        if self.__has_right(idx):
            right_idx = self.__get_right_idx(idx)
            if self.nodes[right_idx] < self.nodes[child_idx]:
                child_idx = right_idx
        
        return child_idx
    
    def __has_left(self, idx: int) -> bool:
        return self.__get_left_idx(idx) < len(self.nodes)
    def __has_right(self, idx: int) -> bool:
        return self.__get_right_idx(idx) < len(self.nodes)


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