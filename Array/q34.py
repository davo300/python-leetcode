# 34. Find First and Last Position of Element in Sorted Array
# Topics: Array, Binary Search

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
    
    def binSearch(self, nums, target, leftBias):
        l,r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m    
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i            

if __name__ == "__main__":
    s = Solution()
    nums = [3,3,3]
    target = 3
    print(s.searchRange(nums, target))  # Output: [3,4]    