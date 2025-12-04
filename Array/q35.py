# 35. Search Insert Position

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0                        # Start of the list
        hi = len(nums) - 1           # End of the list

        while lo <= hi:
            mid = (lo + hi) // 2     # Middle index

            if nums[mid] == target:
                return mid           # Target found, return index
            elif nums[mid] < target:
                lo = mid + 1         # Search right half
            else:
                hi = mid - 1         # Search left half
        # when element is not found, lo always returns 
        # the index of the target element.
        return lo       


if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,6]
    target = 7
    print(s.searchInsert(nums, target))     