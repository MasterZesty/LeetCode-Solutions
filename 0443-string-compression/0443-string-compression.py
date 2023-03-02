class Solution:
    def compress(self, chars: List[str]) -> int:

        
# APPROCH 2 TRIED USING RECURSIVE FEW TEST CASES ARE FAILING
#         def count_group_char(chars,start_index,count,seq_start_index):
#             print(chars,' : ',chars[start_index],seq_start_index,start_index,len(chars))
            
#             # base case
#             if start_index >= len(chars)-1:
#                 if chars[start_index] == chars[start_index-1]:
#                     # print('c',count)
#                     count += 1
#                     if count > 1:
#                         print('base inserting..',count)
#                         t = list(str(count))
#                         # print(t)
#                         temp_index = start_index
#                         for c in t:
#                             chars.insert(temp_index+1,c)
#                             temp_index += 1
                            
#                         start_index = temp_index
#                         # print(chars,' : ',chars[start_index],seq_start_index,start_index,len(chars))
                        
# #                         if len(t) > 9:
# #                             start_index = temp_index
# #                         else:
# #                             start_index = start_index + len(str(count))
#                         if count>9:
#                               del chars[seq_start_index:start_index-len(t)]
#                         else:
#                               del chars[seq_start_index:start_index-1]
                        
                
#                 return
            
#             if chars[start_index] != chars[start_index+1]:
#                 count += 1
#                 print('main inserting..',count)
#                 if count > 1:
#                     t = list(str(count))
#                     temp_index = start_index
#                     for c in t:
#                         temp_index += 1
#                         chars.insert(temp_index,c)
                        
#                     # print('temp_index',temp_index,chars)
#                     start_index = temp_index - len(t)
#                     # print('temp_index',start_index,chars)
                
                
#                 # delete ele
#                 print('deleting..',chars[seq_start_index:start_index],chars)
#                 del chars[seq_start_index:start_index]
#                 print(chars)
                
#                 if count == 1:
#                     start_index += 1
#                 else:
#                     start_index = seq_start_index + len(t) 
                    
#                 count = 0
#                 seq_start_index = start_index
#                 print(chars,' : ',chars[start_index],seq_start_index,start_index,len(chars))
#                 count_group_char(chars,start_index,count,seq_start_index)
                
#             elif chars[start_index] == chars[start_index+1]:
#                     count += 1
#                     start_index += 1
#                     count_group_char(chars,start_index,count,seq_start_index)
                    
            
#         count_group_char(chars,0,0,0)
        
#         print(chars)
        
        
        
# APPROCH 1      
        
        # You must write an algorithm that uses only constant extra space.
        s = ""
        
        counter  = 0
        curr_char = chars[0]
        
        for i in range(len(chars)):
            
            if i != len(chars)-1:
                
                if curr_char != chars[i+1]:

                    counter += 1

                    if counter == 1:
                        s = s + curr_char
                    else:
                        s = s + curr_char  + str(counter)

                    curr_char = chars[i+1]
                    
                    counter = 0
                else:
                    counter += 1
                    
            else:
                
                if chars[i] == curr_char:
                    counter += 1
                    if counter == 1:
                        s = s + curr_char
                    else:
                        s = s + curr_char + str(counter)
                else:
                    s = s + curr_char
                
            #print('for ',i,chars[i],curr_char,counter)
            
        #print(s)
        
        # chars = list(s)
        print(chars)
        
        del chars[:]
            
        for i in list(s):
            chars.append(i)
        
        # return len(chars)
        print(chars)

#         ABOVE CODE IS FINE BUT SPECIFIACLLY WE HAVE TO MODEIFY LIST ITSELF SO i AM THINKING OF WRITING RECURSIVE CODE THAT WILL UPDATE LIST

        

