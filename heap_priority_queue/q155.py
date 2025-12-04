class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return None


# Example usage
if __name__ == "__main__":
    obj = MinStack()
    obj.push(3)
    obj.push(5)
    obj.push(2)
    obj.push(1)
    
    print("Top:", obj.top())       # 1
    print("Min:", obj.getMin())    # 1

    obj.pop()
    print("popped 1")
    print("Top after pop:", obj.top())     # 2
    print("Min after pop:", obj.getMin())  # 2
