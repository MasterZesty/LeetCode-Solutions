class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        Strings word1 and word2 are close $\iff$ the following 2 conditions are satisfied:

        1. Both strings consist of the same letter set.
        2. The frequencies of alphabets of 2 strings are mutual permutations.
        '''
        n1 = len(word1)
        n2 = len(word2)
        
        if n1 != n2:
            return False
        
        if set(word1) != set(word2):
            return False
        
        f1 = {}
        f2 = {}
        
        for w in word1:
            f1[w] = f1.get(w,0) + 1
            
        for w in word2:
            f2[w] = f2.get(w,0) + 1
            
        # we need to take care of second rule and
        # if we want ot satisfy rule we need count of chars mutual
        # that is no matter what chars comes and how many times
        # but overall chars count of w1 and w2 must be same after sort
        # in short freq of alphabets must be mutual permuattaions
        
        
        return sorted(f1.values()) == sorted(f2.values())