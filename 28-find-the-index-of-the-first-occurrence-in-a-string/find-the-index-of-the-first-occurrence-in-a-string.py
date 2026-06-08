class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sol 1 - brute force
        n = len(haystack)
        m = len(needle)
        # print(n,m)
        for i in range(0,n-m+1):
            string_match = True
            # print(i,string_match)
            for m, c in enumerate(needle):
                print(m,c)
                if c != haystack[m+i]:
                    string_match = False

            if string_match:
                return i


        return -1