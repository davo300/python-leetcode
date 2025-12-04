# 703. Kth Largest Element in a Stream

# You should aim for a solution with O(mlogk) time and O(k) space,
# where m is the number of times add() is called, and k represents 
# the rank of the largest number to be tracked (i.e., the k-th largest element).


from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)     # heapq has its own binary tree properties ex. heapify
        while len(self.minHeap) > k:    # CMD-click heapq variable for info about algorithm
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


if __name__ == "__main__":

    k = 3
    nums = [4, 5, 8, 2]
    obj = KthLargest(k, nums)
    print(obj.add(3)); # return 4
    print(obj.add(5)); # return 5
    print(obj.add(10)); # return 5
    print(obj.add(9)); # return 8
    print(obj.add(4)); # return 8