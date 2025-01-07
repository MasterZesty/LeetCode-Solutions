class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        master_string = '_'.join(words)
        ans = []
        # print(master_string)

        for word in words:
            count = master_string.count(word)
            if count > 1:
                ans.append(word)

        return ans