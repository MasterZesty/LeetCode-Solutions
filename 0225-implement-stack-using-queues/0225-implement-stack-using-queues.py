class MyStack:

    #approch 1 : with one queue
    
    def __init__(self):
        self.qa = []
        
    def push(self, x: int) -> None:
        # appned to q a
        self.qa.append(x)
        i = 0
        v = len(self.qa) - 1
        # make last element first and then rearrange que
        while i < v:
            self.qa.append(self.qa.pop(0))
            i += 1

    def pop(self) -> int:
        # if self.empty:
        #     return None
        
        return self.qa.pop(0)

    def top(self) -> int:
        # if self.empty:
        #     return None
        
        return self.qa[0]
        

    def empty(self) -> bool:
        if len(self.qa) != 0:
            return False
        
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()