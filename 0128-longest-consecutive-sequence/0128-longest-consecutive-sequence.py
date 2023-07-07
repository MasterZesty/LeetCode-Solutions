class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        present_hm = {}
        checked_hm = {}
        len_lcs = 0
        
        for i,val in enumerate(nums):
            if val not in present_hm.keys():
                present_hm[val] = True
                
        #print(present_hm)
        
        
        for i,val in enumerate(nums):
            #first check if given no forms starting 
            #of a subsequnce
            if (val-1) not in present_hm.keys():
                #it is start of sequnce
                checked_hm[val] = True
                flag = True
                t_num = val+1
                t_counter = 1
                while flag:
                    if (t_num) in present_hm.keys():
                        #print()
                        checked_hm[t_num]=True
                        t_counter += 1
                        t_num += 1
                    else:
                        flag = False
                if t_counter >= len_lcs:
                    len_lcs = t_counter
                    
                    
        #print(checked_hm,len_lcs)
        
        return len_lcs