class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        # Approch 1 : Recursive solution
        
        # frog at first stone which is at 0 and we want to make
        # next jump which much be k=1 and if not possible return false
        if stones[1]>1:
            return False
        
        @cache
        def jumper(curr_pos, k):
            print(f'curr_pos {curr_pos} | k {k}')

            if curr_pos == stones[-1]:
                print(f'reached the final stone')
                return True

            if curr_pos > stones[-1]:
                print(f'crossed river but not landed on last stone or already visited, not possible to cross river')
                return False


            # jump possibility 1 : k
            next_possible_positon = curr_pos + k
            if next_possible_positon in stones and next_possible_positon > curr_pos:
                if jumper(next_possible_positon, k):
                    return True

            # jump possibility 2 : k - 1
            next_possible_positon = curr_pos + k - 1
            if next_possible_positon in stones and next_possible_positon > curr_pos:
                if jumper(next_possible_positon, k - 1):
                    return True

            # jump possibility 3 : k + 1
            next_possible_positon = curr_pos + k + 1
            if next_possible_positon in stones and next_possible_positon > curr_pos:
                if jumper(next_possible_positon, k + 1):
                    return True

            return False
    
    
        return(jumper(0, 0))
        
        
        