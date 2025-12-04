# Topics: Math, String, Simulation
# use ASCII heavily here

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        def strToint(str):
            res = 0
            i = 0
            while i < len(str):
                res = res * 10 + (ord(str[i]) - ord('0'))    # ord('0') → 48 this is ASCII conversion function
                i += 1
            return res

  
        def intTostr(n):
            if n == 0:
                return '0'
            digits = []
            while n > 0:
                digit = n % 10      # 120 % 10 == 0
                digits.append(chr(ord('0') + digit))  # convert digit to char => 48 + 0 = 48 (0 in ASCII), 48 + 2 = 50 (2 in ASCII)
                n //= 10   # 120 // 10 = 12
            return ''.join(reversed(digits))   #  ['0','2','1'] -> reversed ['1','2','0'] -> ''.join -> '120'
                                        
        # main logic
        num1 = strToint(num1)
        num2 = strToint(num2)
        mult = num1 * num2
        return intTostr(mult)


if __name__ == "__main__":
    s = Solution()
    num1 = "12"
    num2 = "10"
    print(s.multiply(num1, num2))