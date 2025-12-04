class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(x, n):
            if x == 0: return 0                 # base case 1
            if n == 0: return 1                 # base case 2
        
            res = helper(x * x, n // 2)
            return x * res if n % 2 else res    # if n % 2 = 1 this means True
        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res       # 1 / res if n is negative
      
if __name__ == "__main__":
    s = Solution()
    x = 3
    n = 2
    print(s.myPow(x, n))       