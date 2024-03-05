class Solution:
    def bagOfTokensScore(self, tokens, power):
        '''
        Intuition
        Initially, we can observe that the optimal strategy would involve playing tokens that
        consume the least power first, and then utilizing the power gained from those plays to
        play tokens that require more power. This suggests sorting the tokens array.

        Approach
        Sort the tokens array to facilitate playing tokens with the least power requirement first.
        Use two pointers, left and right, representing the indices of the tokens array.
        Iterate through the tokens array while left is less than or equal to right.
        If the power is sufficient to play the token at index left, play it face-up, decrement power, and increment score.
        Otherwise, if the score is greater than 0, play a token face-down, increment power, and decrement score.
        Update the maximum score achieved so far.
        Repeat steps 4-6 until left is greater than right.
        Return the maximum score achieved.
        
        Complexity
        
        Time complexity:
        Sorting the tokens array takes O(nlogn) time.
        The while loop iterates through at most n tokens once, resulting in O(n) time complexity.
        Thus, the overall time complexity is O(nlogn).
        Space complexity:
        The space complexity is O(1)
        since we are not using any additional data structures that grow with the input size.
        '''
        
        tokens.sort()
        score = 0
        max_score = 0
        left = 0
        right = len(tokens) - 1
        
        while left <= right:
            
            if tokens[left] <= power:
                power -= tokens[left]
                left += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
                
            else:
                break
                
        return max_score