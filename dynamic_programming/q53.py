# Topics: Array, Dynamic Programming, Divide & Conquer
# No, your code does not strictly use the 
# sliding window technique, but it is very similar in spirit. 
# It’s Kadane’s algorithm, which is more efficient 
# and tailor-made for this exact problem.

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            maxSub = max(maxSub, curSum)
        
        return maxSub


if __name__ == "__main__":
    s = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(s.maxSubArray(nums))
