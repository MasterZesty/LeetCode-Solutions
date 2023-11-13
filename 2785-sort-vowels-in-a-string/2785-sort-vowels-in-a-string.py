class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        
        # store vowels with index
        vowels_l = {}
        
        for index, char in enumerate(s):
            if char in vowels:
                vowels_l[index] = char
                
        # print(vowels_l)
        
        v = sorted(vowels_l.values())
        k = sorted(vowels_l.keys())
        # print(v,k)
        
        for val,idx in zip(v,k):
            s = s[:idx] + val + s[idx+ 1 :]
        
         
        return s