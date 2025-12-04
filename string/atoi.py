class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0

        i = 0
        n = len(s)
        res = 0
        sign = 1

        # Step 1: Skip leading spaces
        while i < n and s[i] == ' ':       # repeatedly parse whitespace
            i += 1

        # Step 2: Optional sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Parse digits
        while i < n and s[i].isdigit():    # checks if a string is a digit
            res = res * 10 + int(s[i])     # repeatedly parse digits
            i += 1

        res *= sign

        # Step 4: Clamp to 32-bit signed int range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        return res

        


if __name__ == "__main__":
    s = Solution()
    str = "   +0 123"
    print(s.myAtoi(str))