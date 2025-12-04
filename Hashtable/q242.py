# 242. Valid Anagram
# Topics: String, Hash table, Sorting

# from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) # maybe if allowed
        # return Counter(s) == Counter(t) # maybe if allowed

        if len(s) != len(t):   # if length not equal, then cannot be anagrams
            return False
        
        countS, countT = {}, {}   

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)  # create the hashmap for storing the
            countT[t[i]] = 1 + countT.get(t[i], 0)  # frequency of each char in each string. 

        for c in countS:    # ensure the hashmaps have same frequency of each character
            if countS[c] != countT.get(c, 0):
                return False    # if one string has more or less of a character

        return True    # valid anagrams



if __name__ == "__main__":
    sol = Solution()
    s = "anagram"
    t = "nagaram"
    print(sol.isAnagram(s,t))