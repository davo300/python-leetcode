# 347. Top K Frequent Elements
# Topics: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
# Time: O(n)
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]   # list of lists(list of buckets) i.e. [[], [], []]

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # create freqMap
        for n, c in count.items():
            freq[c].append(n)   # append numbers to thier buckets

        res = []
        for i in range(len(freq) - 1, 0, -1):   # reversed, so the highest freq. bucket gets appended first
            for n in freq[i]:
                res.append(n)   # append elements in the highest freq bucket
                if len(res) == k:   # return once k is reache
                    return res
 


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6]
    k = 2
    print(sol.topKFrequent(nums, k))