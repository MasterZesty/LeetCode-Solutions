# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low = 1
        high = n
        
        # handle some erros ref: https://stackoverflow.com/questions/504335/what-are-the-pitfalls-in-implementing-binary-search
        
        # when guess=1
        if guess(1) == 0:
            return 1
        
        # when guess=n
        if guess(n) == 0:
            return n
        
        
        def find_number(low,high):
            
            # do soome stuff
            
            guess_num = (low + high) // 2
            # print("guess_num :",guess_num)
            
            state = guess(guess_num)
            if state == 0:
                # guess_number == actual pick
                # print("-- ",guess_num)
                return (guess_num)
            
            if state == 1:
                # guess_number < actual_pick
                return find_number(guess_num,high)
                
            if state == -1:
                # guess_number > actual_pick
                return find_number(low,guess_num)
                
            
        return(find_number(low,high))
                