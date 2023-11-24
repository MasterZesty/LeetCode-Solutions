class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        
        n = len(piles)
        
        r = n // 3
        
        max_coin = 0
        
        low = 0
        mid = n - 2
        high = n - 1
        
        # print(f'piles : {piles}')
        # print(f'n : {n} | low : {low} mid: {mid} high : {high}')
        
        while r > 0:
            # print(f'{low} {mid} {high} = {piles[low]} {piles[mid]} {piles[high]}')
            
            max_coin += piles[mid]
            
            low += 1
            
            mid -= 2
            high -= 2
            
            r -= 1
            
        return max_coin
        
        
        
        