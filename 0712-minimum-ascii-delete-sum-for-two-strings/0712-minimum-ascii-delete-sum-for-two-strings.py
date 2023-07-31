class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        # wrong approch lack of understding of question
        '''
        hm_s1 = {}
        hm_s2 = {}
        
        for i,val in enumerate(s1):
            hm_s1[val] = hm_s1.get(val,0) + 1
        
        for i,val in enumerate(s2):
            hm_s2[val] = hm_s2.get(val,0) + 1
            
            
        del_chars = ""
        
        for s1_char in hm_s1:
            print(f's1_char : {s1_char}')
            if hm_s1[s1_char] != 0:
                if s1_char not in hm_s2:
                    del_chars = del_chars + hm_s1[s1_char]*s1_char
                    hm_s1[s1_char] = 0
                else:
                    diff = max(hm_s1[s1_char],hm_s2[s1_char]) - min(hm_s1[s1_char],hm_s2[s1_char])
                    del_chars =  del_chars + diff*s1_char
                    hm_s1[s1_char] = 0
                    hm_s2[s1_char] = 0
            

        for s2_char in hm_s2:
            print(f's2_char : {s2_char}')
            if hm_s2[s2_char] != 0:
                if s2_char not in hm_s1:
                    del_chars = del_chars + hm_s2[s2_char]*s2_char
                    hm_s2[s2_char] = 0
        
        print(f's1 : {hm_s1}   |  s2 : {hm_s2} | del_chars : {del_chars}')
        
        sum = 0
        for c in del_chars:
            sum += ord(c)
            
        return sum
        '''
        
        # use concept of Longest Common Subsequence
        # we need to find longest common subsequnce of str1 and str2
        # ref : https://takeuforward.org/data-structure/longest-common-subsequence-dp-25/
        # ref : https://youtu.be/OT6zcEATv1c
        # ref : https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/discuss/3840553/100-DP-VIDEO-Decoding-Approach-to-Minimum-ASCII-Delete-Sum
        
        if len(s1) > len(s2):
            s1, s2 = s2, s1
            
        prev_row = [0] * (len(s2) + 1)
        
        for j in range(1, len(s2) + 1): 
            prev_row[j] = prev_row[j - 1] + ord(s2[j - 1]) 

        for i in range(1, len(s1) + 1): 
            curr_row = [prev_row[0] + ord(s1[i - 1])] 
            for j in range(1, len(s2) + 1): 
                if s1[i - 1] == s2[j - 1]: 
                    curr_row.append(prev_row[j - 1]) 
                else: 
                    curr_row.append(min(prev_row[j] + ord(s1[i - 1]), curr_row[j - 1] + ord(s2[j - 1]))) 
            prev_row = curr_row 

        return prev_row[-1] 
        