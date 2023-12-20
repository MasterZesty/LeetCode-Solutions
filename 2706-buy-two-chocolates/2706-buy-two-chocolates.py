class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        n = len(prices)
        ans = float('inf')
        
        for i in range(n):
            
            for j in range(n):
                
                if i != j:
                    curr_sum = prices[i] + prices[j]
                    
                    if curr_sum <= money:
                        print(f"{i} {j} | {curr_sum} = {prices[i]} + {prices[j]} | {ans}")
                        
                        if curr_sum < ans:
                            
                            ans = curr_sum
                            
        if ans != float('inf'):
            return money - ans
        
        return money