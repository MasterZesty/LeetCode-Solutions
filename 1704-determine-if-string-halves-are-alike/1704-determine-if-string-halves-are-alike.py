class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels =  ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        n = len(s)//2
        
        a = 0
        b = 0
        
        for i,c in enumerate(s):
            
            if i < n:
                if c in vowels:
                    a += 1
                    
            if i >= n:
                if c in vowels:
                    b += 1
        # print(f"a: {a} b: {b}")            
        return a==b
        