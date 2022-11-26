class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        '''
        # raw approch 1
        
        # set default max_profit
        max_profit = max(profit)
        
        n = len(profit)
    
        
        for i in range(n):
            current_startTime = startTime[i]
            current_endTime = endTime[i]
            current_profit = profit[i]
            
            for j in range(i+1,n):
                 print(i,j,n)
                
                if startTime[j] >= current_endTime:
                    print(i,j,n)
                    
                    current_profit += profit[j]
                    
                    current_startTime = startTime[j]
                    current_endTime = endTime[j]
                    
            if current_profit >= max_profit:
                max_profit = current_profit
                    
            print('Temp profit ',current_profit)
                    
        print('profit ',max_profit)
        
        # NOTE : NOT WORKING
        
        '''
        #  approch 2
        # classical 0/1-Knapsack pattern - include current job and try next valid non overlapping job (0/1)
        
        jobs = zip(startTime, endTime, profit)
        
        # sort jobs -first it will sort according to startTime => endTime => profit
        sorted_jobs = sorted(jobs)
        
        n = len(startTime)
        
        dp = [0]*(n+1)
        
        print(sorted_jobs)
        
        # 1. bisect(list, num, beg, end) num => endtime j[0] => start time
        # https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
        # https://docs.python.org/3/library/bisect.html
        
        for i in reversed(range(n)):
            k = bisect_left(sorted_jobs, sorted_jobs[i][1], key=lambda j:j[0])
            dp[i] = max(sorted_jobs[i][2] + dp[k], dp[i+1])
            
        return dp[0]
        
                
                
                