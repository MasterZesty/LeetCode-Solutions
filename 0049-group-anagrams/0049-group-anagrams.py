class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #
        # ref video https://youtu.be/vzdNOK2oB2E
        
        # apporch 1 : this approch fails when empty or duplictaes keys are prent 
        
#         def helper_char_count(word:str):
#             '''
#             returns freqncy count of chars in given word/str
#             '''
#             # if word == "":
#             #     return {"":0}
            
#             char_count = {}
#             for i,val in enumerate(word):
#                 char_count[val] = char_count.get(val,0) + 1
                
#             return char_count
        
#         strs_count = {}
#         count_empty = 0
#         key_duplication = set()
#         key_duplication_count = {}
#         for j, s in enumerate(strs):
#             if s == "":
#                 count_empty += 1
#             else:
#                 strs_count[s] = helper_char_count(s)
            
#         # print(strs_count)
        
#         key_groups = []
#         used_keys = set()
        
#         for key1, value1 in strs_count.items():
#             if key1 not in used_keys:
#                 current_group  = [key1]
#                 for key2, value2 in strs_count.items():
#                     if key1 != key2 and value1 == value2 and key2 not in used_keys:
#                         current_group.append(key2)
#                         used_keys.add(key2)
#                 # print("current_group : ",current_group)
#                 if len(current_group) >= 1:
#                     key_groups.append(current_group)
#                     used_keys.add(key1)

#         # Print the pairs
#         for pair in key_groups:
#             print(pair)
        
#         if count_empty != 0:
#             empty  = ['']*count_empty
#             key_groups.append(empty)    
        
#         return key_groups
    
        # approch 2 
        
        dic={}
        for word in strs:
            sorted_word="".join(sorted(word))
            if sorted_word not in dic:
                dic[sorted_word]=[word]
            else:
                dic[sorted_word].append(word)
        return dic.values()