# 47. Permutations II
# topics: Array, Backtracking, Sorting
# apparently backTrack() can also mean dfs()? depth first search?
# I think they are different search algorithms though

'''
DFS:	
A general graph/tree traversal algorithm. 
Think of it as exploring as far as possible down one path before backing up.
Backtracking:
A form of DFS where you build a solution incrementally, 
and undo (backtrack) when you hit an invalid or complete path. 
Its DFS + undoing choices.
'''

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = { n:0 for n in nums }   # create frequency map
        for n in nums:        # enter the frequency of the elements into the freqMap
            count[n] += 1

        res = []
        perm = []
        count = { n:0 for n in nums }   # create frequency map
        for n in nums:        # enter the frequency of the elements into the freqMap
            count[n] += 1

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    # using recursion here to constantly pop and add back elements to the 
                    # freqMap and check if the len(perm) == len(nums) => means we have 
                    # found a unique permutation.
                    dfs()     
    
                    count[n] += 1   # updating freqMap
                    perm.pop()      

        dfs()
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2]
    print(s.permuteUnique(nums))
