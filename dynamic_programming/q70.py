# 70. Climbing Stairs
# Dynamic Programming Sol
# Use Golden Ratio sol instead! See math folder
# time: O(n)
# space: O(1)
'''
import math
# time: O(logn)
# space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        phi = (1 + sqrt5) / 2
        psi = (1 - sqrt5) / 2
        n += 1
        return round((phi**n - psi**n) / sqrt5)
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
    
if __name__ == "__main__":
    sol = Solution()

    n = 5

    print(sol.climbStairs(n))