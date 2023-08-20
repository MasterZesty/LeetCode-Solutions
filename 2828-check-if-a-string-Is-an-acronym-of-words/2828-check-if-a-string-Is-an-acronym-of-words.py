class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        flag = True
        
        if len(s) != len(words):
            return False
        
        for i,word in enumerate(words):
            try:
                if s[i] != word[0]:
                    return False
            except:
                pass
        
        
        return flag