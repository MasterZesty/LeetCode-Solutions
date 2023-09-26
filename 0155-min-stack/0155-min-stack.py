class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        # check stack is not empty
        if self.stack:
            self.stack.pop()
            

    def top(self) -> int:
        #check stack is not empty
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        #check stack is not empty
        if self.stack:
            return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()