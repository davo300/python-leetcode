class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):     # create frequency maps
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:            # compare the frequency values in each frequency map 
            if countS[c] != countT.get(c,0):
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "rat"
    t = "car"

    print(sol.isAnagram(s,t))
