class Solution:
    def reverseDegree(self, s: str) -> int:
        prod_ans = 0
        for i,c in enumerate(s):
            index_rev_alpha = ord('z') - ord(c) + 1
            index_in_str = i + 1
            # print(f"i:{i} | c:{c} | index_rev_alpha:{index_rev_alpha} | index_in_str:{index_in_str}")

            prod = index_rev_alpha * index_in_str

            prod_ans += prod

        return prod_ans





