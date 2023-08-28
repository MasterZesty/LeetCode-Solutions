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
    
    
# approch 2: if we want to implement 2 queue
# With two queue
#     Push: To push an element, the code transfers all elements from q1 to q2 to maintain order. Then, the new element is enqueued into q1, and finally, elements are transferred back from q2 to q1.

#     Pop: The front element of q1 is dequeued and returned, simulating the pop operation of a stack.

#     Top: The front element of q1 is returned without dequeuing it, representing the top of the stack.

#     Empty: The stack is considered empty if q1 is empty.
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()