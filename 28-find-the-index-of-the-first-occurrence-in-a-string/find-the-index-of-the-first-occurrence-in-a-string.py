class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sol 1 - brute force
        n = len(haystack)
        m = len(needle)
        for i in range(0,n-m+1):
            if haystack[i:i+m] == needle:
                return i

        return -1