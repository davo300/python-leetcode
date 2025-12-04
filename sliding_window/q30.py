'''
Topics:
Hash Table
String
Sliding Window
'''
import collections

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        # Length of each word (assumed all words have same length)
        K = len(words[0])       
        # Total length of the string s
        N = len(s)              
        # Number of words in the list
        W = len(words)          
        # Result list to store starting indices
        ans = []
        
        # Helper function to adjust the counter
        def increment(word, number, count):
            count[word] += number
            if count[word] == 0:
                del count[word]  # Clean up zero counts to simplify later checks

        # Try starting the window at every offset from 0 to K-1 (to catch all word alignments)
        for start in range(K):
            current = start  # Current pointer for the sliding window

            # If the window of W words starting at `start` doesn't fit, skip
            if current + W * K > N:
                continue    
            
            # Initialize a fresh word count map for this window
            count = collections.Counter()
            for word in words:
                count[word] += 1

            # Subtract the first W words in the current window from the count
            for _ in range(W):
                word = s[current:current + K]  # Get the next word from s
                increment(word, -1, count)     # Subtract its count
                current += K

            # If all words matched (count is empty), record the start index
            if len(count) == 0:
                ans.append(current - (W * K))

            # Slide the window one word at a time
            while current + K <= N:
                # Subtract the word entering the window
                word_enter = s[current:current + K]
                increment(word_enter, -1, count)

                # Add back the word that is leaving the window from the left
                word_exit = s[current - (W * K):current - ((W - 1) * K)]
                increment(word_exit, +1, count)

                current += K

                # If all counts zero, valid match found
                if len(count) == 0:
                    ans.append(current - (W * K))

        return ans

if __name__ == "__main__":
    s = Solution()
    str = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(s.findSubstring(str, words))  # Output: [0, 9]
