class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:    # Skip duplicates
                    continue

                lo, hi = j + 1, n - 1
                while lo < hi:
                    total = nums[i] + nums[j] + nums[lo] + nums[hi]

                    if total == target:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1     # Skip duplicates
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1     # Skip duplicates
                    elif total < target:    # logical since the array is sorted
                        lo += 1
                    else:
                        hi -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    nums = [-3,-1,0,2,4,5]
    target = 0
    print(s.fourSum(nums, target))    