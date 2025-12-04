# Question 44. Wildcard Matching
# Dynamic programming used heavily here!
# Watch the youtube video!
# Difficulty: Hard
# This problem uses heavy boolean algebra! ex. True or False == True

'''
  ''    *  
+----+----+
| F  | F  |
| F  | F  |
| F  | F  |

'''

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]     # dp[2][1] = dp[1][1] or dp[2][0] = True or False = True
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n] 
    
    '''
  ''    *  
+----+----+
| T  | T  |
| F  | T  |
| F  | T  |

    '''


if __name__ == "__main__":
    sol = Solution()
    s = "aa"
    p = "*"
    print(sol.isMatch(s,p))  
