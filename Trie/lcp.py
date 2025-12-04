class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        base = strs[0]  # Use the first word as a reference

        for i in range(len(base)):  # Iterate over each character in `base`
            for word in strs[1:]:  # Compare with all other words
                if i == len(word) or word[i] != base[i]:  # Check mismatch
                    return base[0:i]  # Return the prefix up to `i`
        
        return base  # If no mismatch found, return full base
