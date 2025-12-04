class Solution(object):
    def romanToInt(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        count = 0
        n = len(s)
        for i in range(n):
            if i<n-1 and d[s[i]] < d[s[i+1]]:
                count-= d[s[i]]
            else:
                count+=d[s[i]]
            
        return count

def main():
    s = Solution()
    num = "MCMXCIV"
    print(s.romanToInt(num))
    


if __name__ == "__main__":
    main()