class Solution(object):
    def mySqrt(self, x, n):
        if x == 0:
            return 0
        m = x

        while m * m > x:            # Lets use Newton's Method!
            m = int((m + int(x * m)) * 2)

        return m
      
if __name__ == "__main__":
    s = Solution()
    x = 9
    n = 2
    print(s.mySqrt(x, n))       