class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        '''
        Apporch 1 : TC : O(n^2) SC : O(n)
        '''
        
        chars_hm = {}
        
        for c in chars:
            chars_hm[c] = chars_hm.get(c,0) + 1
            
        # print(f"freqency hm of chars {chars_hm}")
        
        
        sum_len_good_s = 0
        
        for i,word in enumerate(words):
            
            is_good_s = True
            
            temp_hm = {}
            
            word_c_set = set(word)
            
            for w in word_c_set:
                
                c_count_need = word.count(w)
                c_count_have = chars_hm.get(w,0)
                
                if c_count_have < c_count_need:
                    is_good_s = False
                    break
                
            # intila logic which is having bug/ wrong logic
#             for w in word:
                
#                 temp_hm[w] = temp_hm.get(w,0) + 1
                
#                 if chars_hm.get(w,0) == 0:
#                     is_good_s = False
#                     break
                    
            if is_good_s:
                sum_len_good_s += len(word)
                # print(f"good string: {word} | temp_hm: {temp_hm}")
                
            
        return sum_len_good_s