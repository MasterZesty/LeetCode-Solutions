class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        Approach
        
        Create a stack decreasingStack to keep track of decreasing elements.
        Initialize maxThirdElement to the minimum possible value.
        Traverse the Array from Right to Left and for each element in the array:
        If the current element is less than maxThirdElement, return true (found a 132 pattern).
        While the stack is not empty and the top element of the stack is less than the current element:
        Update maxThirdElement to the top element of the stack.
        Pop the top element from the stack.
        Push the Current Element onto the Stack.
        If no 132 pattern is found after traversing the array, return false.
        Complexity
        Time complexity: O(N)
        Since we are iterating the array from right to left then it is linear time and all the operations inside the loop are O(1) then final complexity is O(N).
        Space complexity: O(N)
        Since we are maintaining a stack that at any point can have elements equal the elements of the array so complexity is O(N).
        '''
        
        n = len(nums)
        
        if n < 3:
            return False
        
        decreasingStack = []
        
        c = float('-inf')
        
        for a in reversed(nums):
            
            if a < c:
                return True
            
            while decreasingStack and decreasingStack[-1] < a:
                c = decreasingStack.pop()
            
            decreasingStack.append(a)
            
        return False
            
                