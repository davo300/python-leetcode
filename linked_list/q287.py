# 287. Find the Duplicate Number

# Difficulty: Medium

# Topics: Array, Two Pointers, Binary Search, Bit Manipulation, Linked List??? -> (kind of conceptually)

# Time and Space: You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.

from linkedList import ListNode, LinkedList  # remember imports only work in the same folder!!
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


if __name__ == "__main__":

    sol = Solution()
    nums = [1,3,4,2,2]
    print(sol.findDuplicate(nums))  


