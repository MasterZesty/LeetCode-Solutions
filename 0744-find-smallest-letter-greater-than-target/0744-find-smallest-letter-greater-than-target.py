class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        
        i = 0
        j = n - 1
        
        while i <=  j:
            
            mid = (i + j)//2
            # print(f"i{i} j{j} mid{mid}")
            
            if ord(letters[mid]) <= ord(target):
                i = mid + 1
            
            if ord(letters[mid]) > ord(target):
                j = mid - 1
        
        
        # print(f"i{i} j{j} mid{mid}")
        
        # After the while loop, i will point to the smallest letter greater than target.
        return letters[i % n]  #If i goes out of bounds (i.e., i == n), it wraps around to 0