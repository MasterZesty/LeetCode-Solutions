#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        
        no_pair = 0
        freq = {}
        
        for i,v in enumerate(arr):
            b = v
            a = k - b
            
            no_pair += freq.get(a,0)
            freq[v] = freq.get(v,0) + 1
            
                
        return no_pair


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends