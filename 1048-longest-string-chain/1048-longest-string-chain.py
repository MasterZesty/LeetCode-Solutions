class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # refer : https://leetcode.com/problems/longest-string-chain/discuss/4080044/How-we-think-about-a-solution-Beats-97.49-Python-JavaScript-Java-C%2B%2B
        hm_chains = {}
        
        sorted_words = sorted(words, key=len)
        
        for word in sorted_words:
            hm_chains[word] = 1
            
            for i in range(len(word)):
                # generate pred by reomong 1 char
                pred = word[:i] + word[i+1:]
                
                if pred in hm_chains:
                    hm_chains[word] = max(hm_chains[word],hm_chains[pred] + 1)
                    
        return max( hm_chains.values() )