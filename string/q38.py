'''
Now we do a test, if the (n-1)th result is "12212333312111238"(I typed it randomly), 
what is the n th result? Let's count it. one "1", two "2", one "1" , one "2" , four"3" ,
one "1" , one "2", three"1", one "2", one"3" and one "8".
Therefore, the result is "1122111243111231121318"
'''



class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def nextSequence(s):
            res = ""
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                res = res + str(count) + s[i]
                i += 1    
            return res
        # logic start
        currentSequence = "1"
        
        for i in range(2,n+1):
            currentSequence = nextSequence(currentSequence)
        
        return currentSequence

            
        

if __name__ == "__main__":
    s = Solution()
    n = 4
    print(s.countAndSay(n))  

