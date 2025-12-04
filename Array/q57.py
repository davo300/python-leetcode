# 57. Insert Interval
# Topics: Array

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort(key=lambda i: i[0])  # Don’t use spaces around the = sign when used to indicate a keyword argument ex. WRONG: key = lambda i: i[0] ~ PEP 8
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
                
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)   # used when there is a new interval to create [1, 5], [2, 4] = [1, 5]
            else:
                output.append([start, end])  # used when there are no new intervals to create. ex. [1, 5], [7, 8] = [1, 5], [7, 8]

        return output




if __name__ == "__main__":
    s = Solution()
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(s.insert(intervals, newInterval))     # output: [[1,5],[6,9]]
