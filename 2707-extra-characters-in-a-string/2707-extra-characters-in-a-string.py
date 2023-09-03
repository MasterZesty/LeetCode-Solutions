class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # ref : https://leetcode.com/problems/extra-characters-in-a-string/discuss/3990686/Step-by-step-Beginner-Friendlyororfull-explanationoror-DPororEfficient-Easy-to-understand.
        
        # approch 1 : Code Bottom-up dynamic programming - ITERATIVE
        
        dp = [0] * 51  # Initialize an array to store the minimum extra characters.
        n = len(s)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]  # Initialize with one extra character.

            for w in dictionary:
                if i + len(w) <= n and s[i:i + len(w)] == w:
                    dp[i] = min(dp[i], dp[i + len(w)])  # Update if a word in the dictionary is found.

        return dp[0]  # Return the minimum extra characters for the entire string.
    
        # APPROCH 2: Code top-down dynamic programming - RECURSIEV
        '''
        def __init__(self):
            self.dp = [-1] * 51  # Initialize dp array with -1 values

        def minExtraChar(self, s, dictionary):
            return self.minExtraCharHelper(s, dictionary, 0)

        def minExtraCharHelper(self, s, dictionary, i):
            if i == len(s):
                return 0

            if self.dp[i] == -1:
                self.dp[i] = 1 + self.minExtraCharHelper(s, dictionary, i + 1)  # Initialize with one extra character.

                for w in dictionary:
                    if s[i:i+len(w)] == w:
                        self.dp[i] = min(self.dp[i], self.minExtraCharHelper(s, dictionary, i + len(w)))  # Update if a word in the dictionary is found.

            return self.dp[i]  # Return the minimum extra characters starting from position i
        '''

