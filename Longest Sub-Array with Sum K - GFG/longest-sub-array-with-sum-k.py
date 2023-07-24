#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        sum = 0
        maxi = 0
        hmap = {}
        
        for i in range(n):
            
            sum += arr[i]
            
            if sum == k:
                maxi = max(maxi,i+1)
                
            if (sum-k) in hmap.keys():
                maxi =  max(maxi,i-hmap[sum-k])
                
            if hmap.get(sum) == None:
                hmap[sum] = i
                
        return maxi
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends