class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        h = {}      # Num : Index
        n = len(nums)
        s = set()

        for i, num in enumerate(nums):  # creates the hashmap
            h[num] = i

        for i in range(n):
            for j in range(i+1, n):
                desired = -nums[i] - nums[j]
                if desired in h and h[desired] != i and h[desired] != j:
                    s.add(tuple(sorted([nums[i], nums[j], desired])))

        return [list(triplet) for triplet in s]  # Fix: convert set to list of lists    

    # time: O(n^2)
    # space: O(n)   

if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    print(s.threeSum(nums))