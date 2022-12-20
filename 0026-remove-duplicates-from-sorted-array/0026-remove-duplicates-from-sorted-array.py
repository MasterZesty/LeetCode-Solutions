class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''Point to remember : Do not allocate extra space 
           for another array. You must do this by modifying 
           the input array in-place with O(1) extra memory.
        '''
        
        def identify_dup(curr_idx,next_idx,num_list):
            # print('function called!',num_list)
            if next_idx > (len(num_list)-1):
                return
            
            if len(num_list) == 2:
                # print('error list len < 2 :',num_list)
                # handle case
                if num_list[curr_idx] == num_list[next_idx]:
                    num_list.pop(next_idx)
                    return
                else:
                    # print('returning')
                    return
                
            if len(num_list) == 1:
                return
                
        
            # case for which we will delete element
            if num_list[curr_idx] == num_list[next_idx]:
                num_list.pop(next_idx)
                identify_dup(curr_idx,next_idx,num_list)
            
            curr_idx += 1
            next_idx += 1
            if next_idx <= (len(num_list)-1):
                identify_dup(curr_idx,next_idx,num_list)
                
            return
            
        identify_dup(0,1,nums)
        print('list',nums)
                
        