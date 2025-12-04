class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # This Algorithm approximates divsion without using multiplication, division, or mod operators
        d = abs(dividend)
        dv = abs(divisor)
        output = 0

        while d >= dv:      
            tmp = dv
            mul = 1
            while d >= tmp:
                d -= tmp
                output += mul
                mul += mul
                tmp += tmp

        if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend >= 0):
            output = -output

        return min(2147483647, max(-2147483648, output))

if __name__ == "__main__":
    s = Solution()
    dividend = 7
    divisor = -3
    print(s.divide(dividend, divisor))         