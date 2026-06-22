class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm  = {}
        hm_m = {}
        magic_word = 'balloon'
        for w in magic_word:
            hm_m[w] = hm_m.get(w, 0) + 1
        

        for char in text:
            hm[char] = hm.get(char, 0) + 1

        ans = 1000000000

        for key, val in hm_m.items():
            max_f_char = hm.get(key, 0)
            
            if max_f_char == 0:
                return 0

            min_req_f_char = hm_m.get(key, 0)

            if max_f_char < min_req_f_char:
                return 0

            # let check how much words we can make 
            min_word = max_f_char // min_req_f_char
            
            # print(max_f_char,min_req_f_char )
            ans =  min(ans, min_word)
        # print(hm_m, hm)
        return ans