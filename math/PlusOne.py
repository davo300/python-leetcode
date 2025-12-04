class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str, digits)))
        num += 1
        digits = list(map(int, str(num)))
        return digits

def main():
    s = Solution()
    digits = [9,9,9]
    print(s.plusOne(digits))


if __name__ == "__main__":
    main()