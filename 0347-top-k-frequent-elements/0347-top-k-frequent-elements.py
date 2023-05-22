class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashmap with frequncy of elements 
        
        hmap={}
        
        for index,value in enumerate(nums):
            if value not in hmap.keys():
                hmap[value] = 1
                
            else:
                hmap[value] += 1
                
        print('hmap',hmap)
        
        
        # implement priority queue with pririty as frequency
        # ref : https://www.scaler.com/topics/priority-queue-in-python/
        # following code faces due to edge case if val is -ve sort not work 
        # and functinality of priority queue not working properly.
        
        q = []
        
        for key,value in hmap.items():
            q.append((value,key))
            
        print(q)
        q.sort(reverse=True,key=lambda x:x[0])
        
        print('queue:',q) # (frequncy:value)
        
        ans = []
        
        for o in range(k):
            ans.append(q.pop(0)[1])
            
        
        return ans