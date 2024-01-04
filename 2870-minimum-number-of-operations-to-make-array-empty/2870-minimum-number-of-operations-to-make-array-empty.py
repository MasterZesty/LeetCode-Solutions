class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        min_ops = 0
        
        nums.sort()
        # print(f"arr: {nums}")
        
        n = len(nums)
        i = 0
        
        while i < n:
            # print(f"whille i : {i}")
            start = i
            while ( i < n ) and ( i+1 < n ) and ( nums[i] == nums[i+1] ):
                # print(f"incr i: {i}")
                i += 1
            
            end = i
            
            min_ops_i = 0
            
            num_in_group = end - start + 1
            
            if num_in_group == 1:
                return -1
            
            min_ops_i = (num_in_group)//3 + 1
                
            if num_in_group%3 == 0:
                min_ops_i = min( (num_in_group)//3, min_ops_i)
                
            print(f"nums[i] : {nums[i]} of num_in_group : {num_in_group} for min_ops_i : {min_ops_i}")
            min_ops += min_ops_i
            
            i += 1
            
        print(f"arr: {nums}")
        
        return min_ops
            