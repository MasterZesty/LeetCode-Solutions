class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [n]*m # Each row initially needs `n` elements to complete.
        cols = [m]*n # Each column initially needs `m` elements to complete.

        hm = {}

        for i in range(m):
            for j in range(n):
                hm[mat[i][j]] = (i,j)

        # print(f"hm:{hm}")
        ans = -1

        for i, v in enumerate(arr):
            r, c = hm.get(v)
            rows[r] -= 1
            cols[c] -= 1
            # print(f"i:{i} rows:{rows} cols:{cols}")
            if rows[r] == 0 or cols[c] == 0:
                ans = i
                break

        # print(f"rows:{rows} cols:{cols}")


        return ans