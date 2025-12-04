class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        res = ""

        # Step 1: Convert string to zig zag form depending on the number n
        for r in range(numRows):
            increment = (numRows - 1) * 2  
            # range(start, stop, step) # step/increment is what gets added to i each iteration of the loop
            for i in range(r, len(s), increment): 
                res += s[i]
                if (r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s)):
                    res += s[i+increment - 2 * r]
                    
        return res




if __name__ == "__main__":
    s = "PAYPALISHIRING"
    n = 4
solution = Solution()
ans = solution.convert(s,n)
print(ans)
