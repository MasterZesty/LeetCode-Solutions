class Solution:
    def totalMoney(self, n: int) -> int:
        
        # this hm only for understanding not needed in solution
        # d = {
        #     0:"Monday",
        #     1:"Tuesday",
        #     2:"Wednesday",
        #     3:"Thursday",
        #     4:"Friday",
        #     5:"Saturday",
        #     6:"Sunday"
        # }
        
        total_money = 0
        
        days = 0
        monday_money = 1
        day_money = 0
        
        for i in range(n):
            
            if days > 6:
                days = 0
                monday_money += 1
                day_money = monday_money
                
            
            if days == 0:
                total_money += monday_money
                day_money = monday_money
                # print(f"for {d[days]} | i : {i} days : {days} | day_money : {day_money}")
                days += 1
                continue
            
            day_money += 1
            
            total_money += day_money
            
            # print(f"for {d[days]} | i : {i} days : {days} | day_money : {day_money}")
            
            days += 1
            
        return total_money
                
            