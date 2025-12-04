# 739. Daily Temperatures
# Topics: Array, Stack, Monotonic Stack, Weekly Contest 61
# Difficulty: Medium


from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)   # make the size of res equal to the size of the temperatures list
        stack = []

        for i, t in enumerate(temperatures):  # enumerate is Python shorthand for looping through a list with both the index and the value.
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()  # pop the current (temp, index) pair from the top of the stack
                res[stackInd] = (i - stackInd)  # the result element is the difference between the current index and the popped stack index
            stack.append([t, i])   # if the current temp is not greater than the top of the stack temp.
        
        return res      # return the list of the differences between the days of greater temperatures
            


        
        
if __name__ == "__main__":
    sol = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(sol.dailyTemperatures(temperatures))