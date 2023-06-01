class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr, n):
        # Code here
        max_dis = 0
        
        first_occ = {}
        
        for idx,num in enumerate(arr):
            if num not in first_occ.keys():
                first_occ[num] = idx
                
            else:
                t_dis = idx - first_occ[num]
                if t_dis > max_dis:
                    max_dis = t_dis
                    
                    
        return max_dis



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.maxDistance(arr, n))
# Contrbuted By:Harshit Sidhwa


# } Driver Code Ends