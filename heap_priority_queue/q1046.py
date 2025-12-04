# 1046. Last Stone Weight

# You should aim for a solution as good or 
# better than O(nlogn) time and O(n) space, 
# where n is the size of the input array.

# MinHeap multiply by -1 to create MaxHeap

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]       # MinHeap multiply by -1 to create MaxHeap
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])


if __name__ == "__main__":

    sol = Solution()
    stones = [2,7,4,1,8,1]
    print(sol.lastStoneWeight(stones))  