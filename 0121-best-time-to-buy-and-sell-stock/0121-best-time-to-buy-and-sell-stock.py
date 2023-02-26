class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
#         following code is of O(n) but still gives TLE

#         max_profit = 0
        
#         for i,val_i in enumerate(prices):
#             if (i == len(prices)-1):
#                 # print(i,prices[i:])
#                 break
#             sell_max_val = max(prices[i+1:])
#             if sell_max_val > val_i:
#                 max_profit = max(max_profit,(sell_max_val - val_i))
                    
#         # print(max_profit)
        
#         return max_profit

        # left = 0 #Buy
        # right = 1 #Sell
        # max_profit = 0
        # while right < len(prices):
        #     currentProfit = prices[right] - prices[left] #our current Profit
        #     if prices[left] < prices[right]:
        #         max_profit =max(currentProfit,max_profit)
        #     else:
        #         left = right
        #     right += 1
        # return max_profit
        
        max_profit = 0
        left_buy = 0
        right_sell = 1
        
        while right_sell < len(prices):
            current_profit = prices[right_sell] - prices[left_buy]
            if prices[right_sell] > prices[left_buy]:
                max_profit = max(current_profit,max_profit)
            else:
                left_buy = right_sell
                
            right_sell += 1
            
        return max_profit
            