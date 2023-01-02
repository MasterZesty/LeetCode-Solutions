#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        
        
        # recursive solution not optimized ==> memoization
        
        rows, cols = (n+1, W+1)
        global t 
        t = [[-1 for i in range(cols)] for j in range(rows)]
        # print(t)
        
        
        
        def knapsack(wt,val,W,n):
            
            global t
            
            # write base case
            if n == 0 or W == 0:
                return 0
                
            if t[n][W] != -1:
                return t[n][W]
                
            if wt[n-1] <= W:
                t[n][W] = max( ( val[n-1] + knapsack(wt,val,W-wt[n-1],n-1) ) , knapsack(wt,val,W,n-1) )
                return t[n][W]
                
            if wt[n-1] > W:
                t[n][W] = knapsack(wt,val,W,n-1)
                return t[n][W]
                
            
        return knapsack(wt,val,W,n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends