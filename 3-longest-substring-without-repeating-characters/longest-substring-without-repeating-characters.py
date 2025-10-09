class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)

        for curr_index in range(n):
            char_count = {}
            char_count[s[curr_index]] = 1
            curr_max_len = 1

            for next_index in range(curr_index+1,n):

                char_count[s[next_index]] = char_count.get(s[next_index],0) + 1
                if char_count[s[next_index]] > 1:
                    break
                else:
                    curr_max_len += 1

            max_len = max(max_len, curr_max_len)

        
        return max_len