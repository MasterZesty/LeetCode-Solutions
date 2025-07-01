class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        no_possible_s = 1
        
        prev_c = word[0]

        for i in range(1, n):
            curr_c = word[i]

            if curr_c == prev_c:
                no_possible_s += 1

            prev_c = curr_c

        return no_possible_s