class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        s_dict = {}
        t_dict = {}
        
        if len_s == len_t:
            for (char_s,char_t) in zip(s,t):
                if char_s not in s_dict.keys():
                    s_dict[char_s] = 1
                else:
                    s_dict[char_s] += 1
                    
                if char_t not in t_dict.keys():
                    t_dict[char_t] = 1
                else:
                    t_dict[char_t] += 1
                    
        else:
            return False
        
        # print("s",s_dict)
        # print("t",t_dict)
        
        return(s_dict == t_dict)
                    
                
        
        