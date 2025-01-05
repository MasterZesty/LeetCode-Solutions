class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        dp = [0]* (n+1)

        for shift in shifts:
            start, end, direction = shift

            if direction == 1:
                dp[start] += 1
                dp[end+1] -= 1

            if direction == 0:
                dp[start] -= 1
                dp[end+ 1] += 1

        prefix_sum = 0
        s = list(s)

        for i in range(n):
            prefix_sum += dp[i]
            current_pos = ord(s[i]) - ord('a')
            new_pos = (current_pos + prefix_sum%26 + 26) % 26
            s[i] = chr(ord('a') + new_pos)

        return ''.join(s)