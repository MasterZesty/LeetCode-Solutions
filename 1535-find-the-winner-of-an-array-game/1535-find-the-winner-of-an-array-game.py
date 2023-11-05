class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        '''
        naive brute force apporch
        TC : O(n)
        SC : O(1)
        '''
        curr_winner = arr[0]
        count = 0
        for i in range(1,len(arr)):
            if arr[i] > curr_winner:
                curr_winner = arr[i]
                count = 1
            else:
                count += 1
                
            if count == k:
                return curr_winner
            
        return curr_winner