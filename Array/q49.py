# 49. Group Anagrams
# Topics: Array, Hash Table, String, Sorting
# Time: O(m * n) where m is the number of strings
# and n is the average number of characters in each string.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26    # character frequency from 'a' to 'z'

            for c in s:
                count[ord(c) - ord("a")] += 1   # compute the difference between current char and 'a' the start to get the ascii decimal value and increment by 1
            
            res[tuple(count)].append(s)  # convert count list to a tuple, then append the current string to the tuple, ex. "eat" and "tea" get added to the same list because both of their keys are equal.
        # list() wrapper function turns dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]) --> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        return list(res.values())  # Convert to list before returning
    
if __name__ == "__main__":
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(sol.groupAnagrams)