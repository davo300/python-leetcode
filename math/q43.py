# Topics: Math, String, Simulation
# we simulate multiplication without a calculator here
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2)) # create res = c
        num1, num2 = num1[::-1], num2[::-1] # reverse both strings ex. "123" -> "321"
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])   # digit = 3 * 6 = 18
                res[i1 + i2] += digit   # res[0] = 0 + 18 -> res = [18, 0, 0, 0, 0, 0]
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)  # res[1] = 0 + 1 = 1 -> res = [18, 1, 0, 0, 0, 0]
                res[i1 + i2] = res[i1 + i2] % 10    # res = [8, 1, 0, 0, 0, 0]

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)    
'''
res[beg:] is a slice of the result list — a list of digits (like [1, 2, 3])
map(str, res[beg:]) applies str() to each digit, converting them to characters:
[1, 2, 3] → ['1', '2', '3']
"".join(['1', '2', '3']) → "123"
'''

if __name__ == "__main__":
    s = Solution()
    num1 = "123"
    num2 = "456"
    print(s.multiply(num1, num2))