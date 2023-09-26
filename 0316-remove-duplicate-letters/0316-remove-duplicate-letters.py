class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # ref ; https://leetcode.com/problems/remove-duplicate-letters/discuss/1859515/Python-oror-O(n)-Beats-98-oror-Stack-oror-Detailed-Explanation-oror-Simple
        last_occ ={}
        stack = []
        visited = set()
        
        n =len(s)
        
        # keep record of each char's last occurance so that
        # using this will avoid to delete this char too early
        for i in range(n):
            last_occ[s[i]] = i
            
        for i in range(n):
            
            if s[i] not in visited:
                
                '''
                This part checks if there are letters in the stack (our stack of blocks), and 
                if the last letter on the stack is greater (comes later in the alphabet) than the 
                current letter we're looking at, AND if we're going to see that last letter again 
                in the future (to avoid removing it too early).

                If all these conditions are met, we can take the last letter off the stack 
                because it's safe to remove it.
                '''
                while( stack and stack[-1] > s[i] and last_occ[stack[-1]] > i ):
                    visited.remove( stack.pop() )
                
                stack.append(s[i])
                visited.add(s[i])
                
        return ''.join(stack)
        