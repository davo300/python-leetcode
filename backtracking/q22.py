class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add open parentheses if open < n
        # only add a closing parentheses if closed < open
        # valid if open == closed == n
        # this algorithm uses a stack and tree diagram to find a solution and use recursion to 
        # backtrack to previous elements of the tree and then find those solutions.
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:   # base case
                res.append("".join(stack))  # where we create the result strings
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()     # pop the current parentheses when we have returned

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()     # pop the current parentheses when we have returned
        
        backtrack(0,0)

        return res


if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.generateParenthesis(n))   