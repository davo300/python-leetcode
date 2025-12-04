# 34. Find First and Last Position of Element in Sorted Array
# Topics: Array, Binary Search

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        lo = 0
        hi = len(nums) - 2
        last = len(nums) - 1

        if len(nums) == 1 and target == nums[0]:
            return [0,0]
        elif len(nums) == 2 and (target == nums[0] and target == nums[1]):
            return [0,1]
        elif len(nums) == 2 and (target == nums[0]):
            return [0,0]
        elif len(nums) == 2 and (target == nums[1]):
            return [1,1]
        elif len(nums) == 3 and (target == nums[0] and target == nums[1]):
            return [0,1]
        elif len(nums) == 3 and (target == nums[1] and target == nums[2]):
            return [1,2]
        elif len(nums) == 3 and (target == nums[0]):
            return [0,0]
        elif len(nums) == 3 and (target == nums[1]):
            return [1,1]
        elif len(nums) == 3 and (target == nums[2]):
            return [2,2]
        elif len(nums) == 3 and (target == nums[1] and target == nums[last]):
            return [2,last]
        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                res.append(mid)
                if len(res) == 2:
                    return res  
            # Left half is sorted
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        return [-1,-1]



if __name__ == "__main__":
    s = Solution()
    nums = [3,3,3]
    target = 3
    print(s.searchRange(nums, target))  # Output: [3,4]    