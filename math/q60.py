# 60. Permutation Sequence
# Topics: Math, Recursion
# Difficulty: Hard

from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        ans = ""
        nums = list(range(1, n + 1))    # create list from 1 to n + 1 ex. n = 3 -> nums = [1,2,3] -> n + 1 -> 3 in range() function
        k -= 1      # include 0th element

        for i in range(1, n + 1):
            index = 0
            cnt = factorial(n - i)  # 0! = 1

            index = k // cnt        # index is the current index of nums that we wish to add to string
            k -= index * cnt

            ans += str(nums[index])
            del nums[index]         # delete index value since we already added it to the string
        
        return ans
                

if __name__ == "__main__":
    s = Solution()
    n = 3
    k = 3
    print(s.getPermutation(n,k))

    
