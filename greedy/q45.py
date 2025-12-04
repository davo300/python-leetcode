# 45. Jump Game II ~ Greedy ~ O(n) time
# Should be solved after 55. Jump Game

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0 
        l = r = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1

        return res    

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,0,1,4]
    print(s.jump(nums))
