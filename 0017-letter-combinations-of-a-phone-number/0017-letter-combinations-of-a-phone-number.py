class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hm = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        combinations = []
        
        n = len(digits)
        
        if n == 0:
            return []
        
        if n == 1:
            return [x for x in  hm[digits]]
        
        # ref : https://stackoverflow.com/questions/798854/all-combinations-of-a-list-of-lists
        def combine(terms, accum):
            
            last = (len(terms) == 1)
            n = len(terms[0])
            for i in range(n):
                item = accum + terms[0][i]
                if last:
                    combinations.append(item)
                else:
                    combine(terms[1:], item)
        
        terms = []
        for i in digits:
            terms.append([x for x in hm[i]])
            
        combine(terms, '')
        
        return combinations