class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        number = 1
        while k != 0:
            print('number',number)
            if number not in arr:
                print('num not in arr:',number)
                k -= 1
                
            number += 1
            
        return (number-1)