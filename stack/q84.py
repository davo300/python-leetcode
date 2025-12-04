# 84. Largest Rectangle in Histogram
# Topics: Array, Stack, Monotonic Stack
# Difficulty: Hard

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []      # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:  # stack stores (index, height) pairs, so stack[-1][1] accesses the height of the top element
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
 

        
if __name__ == "__main__":
    sol = Solution()
    heights = [2,1,5,6,2,3]
    print(sol.largestRectangleArea(heights))