class Solution:
    def countOrders(self, n: int) -> int:
        # Aprroch : ref: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/4024280/99.57-DP-and-Math-and-Recursion
        
        '''
        let us assume we are at ith order
        * there are i pickups and i delivery so total 2i positions
        * for pickup - we can place pikup at 2i - 1 postion as last position in not possible hence -1
        * for delivery - we can place delivery we have i choices beacuse it Di must come after Pi hence i
        * so possible sequnces = (2i - 1)*i
        * Multiply your current count by (2i - 1) * i to get the new count. This gives you the total number of sequences for i orders.
        '''
        MOD = 10**9 + 7
        
        count = 1
        
        for i in range(2,n+1):
            
            count = ( count * ((2*i - 1)*i) ) % MOD
        
        
        return count