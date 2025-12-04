# 128. Longest Consecutive Sequence
# Topics: Array, Hash Table, Union Find

'''
🎯 The key idea:
You only run the while loop to grow a sequence when you’re at the first number of that sequence.
Once that sequence is counted starting from n, we’ll skip all the other numbers in that sequence 
because their (n - 1) is present in the set.

✅ So "when is it ensured?"
It's ensured at runtime by the if (n - 1) not in numSet: check — it blocks any attempt to 
reprocess a number that is not the start of a new sequence.
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:    # ✅ Iterate over set to avoid duplicates
            # check if its the start of the sequence
            if (n - 1) not in numSet:   
                length = 0
                while (n + length) in numSet:
                    length += 1                 # this is where we compute the length of the nums in numSet
                longest = max(length, longest)  # what is the longest length?
        return longest

if __name__ == "__main__":
    sol = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(sol.longestConsecutive(nums))