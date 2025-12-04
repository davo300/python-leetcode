class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1       # create a sign variable and multiply later on
        MIN =  -2147483648
        MAX = 2147483647
        x = abs(x)


        res = 0
        while x:
            digit = x % 10              # python can't handle -1 % 10 = 9
            x = x // 10                 # python can't handle -1 // 10 = -1
            
            if (res > MAX // 10 or 
                (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or 
                (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit

        return sign * res

if __name__ == "__main__":
    s = Solution()
    num = -231
    print(s.reverse(num))