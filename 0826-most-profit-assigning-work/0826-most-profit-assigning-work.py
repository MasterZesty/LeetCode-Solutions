class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # https://leetcode.com/problems/most-profit-assigning-work/discuss/126932/Python-sort-based
        # https://stackoverflow.com/questions/9764298/given-parallel-lists-how-can-i-sort-one-while-permuting-rearranging-the-other
        njobs = len(difficulty)
        mworkers = len(worker)
        
        # list1, list2 = zip(*sorted(zip(list1, list2)))
        difficulty, profit = zip(*sorted(zip(difficulty, profit)))
        
        # typeerror - tuple does not support oject assignent
        profit = list(profit)
        
        max_profit = float('-inf')
        # profits array can be modified to store the max_profits till that index.
        for i in range(len(profit)):
            if max_profit < profit[i]:
                max_profit = profit[i]
                
            else:
                profit[i] = max_profit
        
        
        from bisect import bisect_right
        
        max_p = 0
        for w in worker:
            pos = bisect_right(difficulty, w)
            
            if pos != 0:
                max_p += profit[pos-1]
            
            
        return max_p