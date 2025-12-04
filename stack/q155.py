# self.minStack[-1] is the top element

class MinStack:

    def __init__(self):
        self.stack = []         # the key to the stack data structure is two stacks
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:   # if minStack has elements
            val = min(val, self.minStack[-1])   # self.minStack[-1] is the top element
        else:
            val = val   
        self.minStack.append(val)   # after top of minStack is determined, we can append it to minStack

    def pop(self) -> None:
        self.stack.pop()    # pop top element from both stacks
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]   # top of stack

    def getMin(self) -> int:
        return self.minStack[-1]  # smallest element in stack



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin() )   # return -3
    obj.pop()
    print(obj.top())     # return 0
    print(obj.getMin())    # return -2