# 973. K Closest Points to Origin


from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res

if __name__ == "__main__":

    sol = Solution()
    points = [[1,3],[-2,2]]
    k = 1
    print(sol.kClosest(points, k))  