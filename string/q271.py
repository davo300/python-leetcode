# 271. Encode and Decode Strings

# Topics: String...?

# difficulty: Medium

# Recommended Time & Space Complexity:
# You should aim for a solution with O(m) time for each encode() and decode() 
# call and O(m+n) space, where m is the sum of lengths of all the strings 
# and n is the number of strings.



from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        # this code transforms list of strings into 1 single string
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s    # use the # (pound) symbol and string length to signify the start of a string 
        return res              
    

    def decode(self, s: str) -> List[str]:
        # this code transforms 1 single string back into a list of strings
        res, i = [], 0
        
        while i < len(s):       # this loop locates the strings and puts it back in array form
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res



if __name__ == "__main__":
    sol = Solution()
    input = ["neet", "code", "love", "you"]
    encoded = sol.encode(input)
    print("Encoded:", encoded)
    decoded = sol.decode(encoded)
    print("Decoded:", decoded)
