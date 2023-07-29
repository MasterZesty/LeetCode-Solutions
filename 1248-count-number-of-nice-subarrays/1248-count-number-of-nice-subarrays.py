class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #brute froce approch
        
        # hashmap approch
        s = 0 # running sum
        c = 0 # count of subaaray
        hm = {} # hashmap to store
        
        for i,val in enumerate(nums):
            print(f'{val}')
            flag = 0
            
            if val % 2 != 0:
                flag = 1
                
            print(f'i {i} val {flag}')
            
            s += flag
            
            if s == k:
                c+= 1
            
            # checking if we get any sum which is s-k which ensures we
            # are having subarray with sum k
            c += hm.get(s-k,0)
            
            hm[s] = hm.get(s,0) + 1
        
            
        print(f'{nums}')     
        
        
        
        
        return c