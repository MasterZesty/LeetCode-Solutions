import math
from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),  (0, 0),  (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        smooth_img = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                count = 0
                total = 0

                for dx, dy in directions:
                    new_i, new_j = i + dx, j + dy
                    if valid(new_i, new_j):
                        total += img[new_i][new_j]
                        count += 1

                smooth_img[i][j] = math.floor(total / count)

        return smooth_img
