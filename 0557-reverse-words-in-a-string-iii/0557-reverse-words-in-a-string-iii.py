class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        t = [x[::-1] for x in words]
        
        #print(t,words)
        
        return ' '.join(t)