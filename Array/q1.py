from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}  # number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hmap:
                return [hmap[complement], i]
            hmap[num] = i  # store the index of the current number
        return []  # in case no solution is found

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))  # Output: [0, 2]
