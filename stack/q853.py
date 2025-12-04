# 853. Car Fleet
# Topics: Array, Stack, Sorting, Monotonic Stack, Weekly Contest 89
# Difficulty: Medium
# Time: O(n)

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]    # pair = [[0, 4], [2, 2], [4, 1]]

        stack = []
        for p, s in sorted(pair)[::-1]:     # Reverse sorted order. The sorted() function in Python returns a new sorted list from the elements of any iterable (like a list, tuple, or string), without modifying the original
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:  # stack[-1] is the top of the stack
                stack.pop()     # pop off the top: 2 cars => 1 fleet

        return len(stack)   # len(stack) is the number of car fleets calculated amond all the (position, speed) pairs.


        
        
if __name__ == "__main__":
    sol = Solution()
    target = 12
    position = [10,8,0,5,3] 
    speed = [2,4,1,1,3]
    print(sol.carFleet(target, position, speed))