# O(n) greedy solution is faster than O(n^2) dynamic programming solution
# basically we iterate through the array moving in reverse order
# setting the new goal every time the current element
# can jump to the previous element.
# if goal == 0 index then return True, meaning we can jump from the first
# index to the last index.


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i        # set new goal post

        return True if goal == 0 else False

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,1,1,4]
    print(s.canJump(nums))
