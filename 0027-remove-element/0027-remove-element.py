class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        def remove_occ(nums_list,val,idx):
            # print('funct called : ',nums_list,idx)
            if idx == (len(nums_list)):
                # print('retn ',idx)
                return
            
            if nums_list[idx] == val:
                # print('rm: ',nums_list[idx],val)
                nums_list.pop(idx)
                remove_occ(nums_list,val,idx)
            else:
                idx += 1
                remove_occ(nums_list,val,idx)
            
            
            
        remove_occ(nums,val,0)
        # print(nums)