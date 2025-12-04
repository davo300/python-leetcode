class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Function to calculate sum of squares of digits of a number
        def get_next(num):
            total_sum = 0
            while num > 0:
                digit = num % 10
                total_sum += digit * digit
                num //= 10
            return total_sum
        
        # Floyd's Tortoise and Hare approach (Cycle Detection)
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)  # Move slow pointer by one step
            fast = get_next(get_next(fast))  # Move fast pointer by two steps
        
        return fast == 1  # If fast reaches 1, it’s a happy number
    

def main():
    s = Solution()
    print(s.isHappy(2))  # Should print True because 19 is a happy number

if __name__ == "__main__":
    main()