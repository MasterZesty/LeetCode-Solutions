class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)

        for i in range(n):
            char_count = {}
            char_count[s[i]] = 1
            curr_max_len = 1

            for j in range(i+1,n):

                char_count[s[j]] = char_count.get(s[j],0) + 1
                # print(f"chars: {s[i:j]} | {char_count}")
                if char_count[s[j]] > 1:
                    # print(f"chars: {s[i:j]} | {char_count}")
                    break
                else:
                    curr_max_len += 1

                # print(f"{i} {j} :curr_max_len: {curr_max_len}")

            max_len = max(max_len, curr_max_len)

        
        return max_len