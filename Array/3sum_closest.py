# This program finds the sum of three numbers that is closest to the target value
# We can use two pointers hi and lo to traverse the array of integers
# Time: O(n^2)
# Space: O(n)


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i + 1, n - 1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]

                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum

                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1

        return closest_sum
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,4]
    target = 5
    print(s.threeSumClosest(nums, target))    
