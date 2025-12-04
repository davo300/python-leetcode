# difficulty: Hard
# 41. First Missing Positive
# 3 loops, O(3n) => O(n) time
# O(1) memory
# topics: Array, Hash table

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1) 

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i
        return len(nums) + 1
        

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,2]
    print(s.firstMissingPositive(nums))