# 150. Evaluate Reverse Polish Notation
# Topics: Array, Math, Stack
# Reverse Polish Notation also called Postfix notation


from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:       # create a set of operators
                b = stack.pop()     
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Truncate toward zero (like in Leetcode)
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]

        
        
if __name__ == "__main__":
    sol = Solution()
    tokens = ["4","13","5","/","+"]
    print(sol.evalRPN(tokens))