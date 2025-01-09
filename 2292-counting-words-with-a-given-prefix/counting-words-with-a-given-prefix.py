class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(words)
        ans = 0

        for word in words:

            if word.startswith(pref):
                ans+= 1

        return ans