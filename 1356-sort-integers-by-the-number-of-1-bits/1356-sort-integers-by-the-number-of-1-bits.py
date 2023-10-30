class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        '''
        Time complexity: The time complexity of the sorted function is $$O(n \log n)$$, 
        where $n$ is the length of the array. Counting the 1's in the binary representation 
        of each number can be done in $O(m)$ time, where $m$ is the maximum number of bits 
        needed to represent any number in the list. Thus, the overall time complexity is 
        $O(n \log n \times m)$.
        
        Space complexity: The space complexity of the sorted function is $O(n)$, as it 
        returns a new sorted list.
        '''
        return sorted(arr, key = lambda x: ( bin(x).count('1'), x)  )