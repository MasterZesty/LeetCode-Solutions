class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        '''
        # approch 1 : brute force TC : O(n) SC:O(1)
        # correction : The time complexity is O(n^2) due to the two functions count_loss_shop_closed and count_loss_shop_open. For each closing hour 'i', these functions perform           # string slicing and then call the count method on the sliced strings. The count method itself takes O(m) time, where 'm' is the length of the sliced string. Since you are         # calling these functions inside a loop that runs 'n' times, the total time complexity becomes O(n^2).
        
        def count_loss_shop_closed(closing_hour):
            # penalty when the shop is closed at jth hour
            # and customers come 'Y'
            return customers[closing_hour:].count('Y')
        

        def count_loss_shop_open(closing_hour):
            # penalty when the shop is closed at jth hour
            # and customers come 'Y'
            return customers[:closing_hour].count('N')
        
        n = len(customers)
        min_penalty = 1e5
        min_hour = n
        for i in range(n+1):
            penalty = count_loss_shop_closed(i) + count_loss_shop_open(i)
            
            if penalty < min_penalty:
                min_penalty  = penalty
                min_hour = i
                    
            #print(f'for {i} th hour penalty is {penalty} | curr min penalty {min_penalty} min_hour {min_hour}')
                    
        return min_hour
        '''
        
        
        # approch 2 : TC: O(n)
        # ref: https://leetcode.com/problems/minimum-penalty-for-a-shop/discuss/3974425/95-faster-oror-Java-oror-C%2B%2B-oror-Easy-to-undersatnd-oror-Simple
        max_score = score = 0
        best_hour = -1

        for i, c in enumerate(customers):
            score += 1 if c == 'Y' else -1
            if score > max_score:
                max_score, best_hour = score, i
                
        return best_hour + 1
        
        
        
        # approch 3 : convert apporch 1 to O(n)
