class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # ref vid : https://youtu.be/IAYKQbZoZRg?si=An0LY-dqgkfZDL0f
        # ref :https://leetcode.com/problems/binary-trees-with-factors/discuss/4209329/video-walkthrough-beats-99-with-readable-code-oror-explained-by-FAANG-engineer
        # ref : https://leetcode.com/problems/binary-trees-with-factors/discuss/4209092/Efficient-Methodor-Explained-Intuition-and-Approach-or-Java-or-C%2B%2B-or-Python-or-JavaScript-or-C-or-PHP
        arr.sort()
        dct = {elem: 1 for elem in arr}
        for elem in arr:
            for factor in arr:
                if factor == elem:
                    break
                if elem % factor == 0 and elem // factor in dct:
                    dct[elem] += dct[factor] * dct[elem // factor]
        return sum(dct.values()) % (pow(10, 9) + 7)