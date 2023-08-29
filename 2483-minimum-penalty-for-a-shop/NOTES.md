```
def bestClosingTime(self, customers: str) -> int:
# approch 1 : brute force TC : O(n) SC:O(1)
def count_loss_shop_closed(closing_hour):
# penalty when the shop is closed at jth hour
# and customers come 'Y'
return customers[closing_hour:].count('Y')
​
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
print(f'for {i} th hour penalty is {penalty} | curr min penalty {min_penalty} min_hour {min_hour}')
return min_hour
```
​
* as 1 <= customers.length <= 10^5 we need to reduce TC