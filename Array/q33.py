# Topics: Array, Binary Search
# Medium difficulty

'''
Original sorted:   [0, 1, 2, 4, 5, 6, 7]
Rotated version:   [4, 5, 6, 7, 0, 1, 2]
                             ↑  ↑
                            lo mid                          
'''
# The key of this binary search problem is to be able to handle
# arrays that have a rotation in it


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
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
        return -1



if __name__ == "__main__":
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(s.search(nums, target))  # Output: 4    