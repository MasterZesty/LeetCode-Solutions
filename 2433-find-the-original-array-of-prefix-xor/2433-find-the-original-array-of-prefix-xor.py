class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n =len(pref)
        
        arr = [0 for i in range(n)]
        
        arr[0] = pref[0]
        
        for i in range(1,n):
            
            #print(f'i : {i} : {arr[i-1]} ^ {pref[i]} -> {arr[i-1] ^ pref[i]}')
            arr[i] = pref[i-1] ^ pref[i]
            
            
        #print(f'ans : {arr}')
        
        return arr
        
        