class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
        count = 0
        i = 1
        while i < len(word):
            
            if abs( ord(word[i]) - ord(word[i-1]) ) <= 1:
                count += 1
                i +=1
                
            i += 1
                
        return count
                
                
                
        