class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        ones = []
        for i, box in enumerate(boxes):
            # print(i,box)
            if box == '1':
                ones.append(i)

        # print(f"ones:{ones}")

        ans = [0]*n

        for i, box in enumerate(boxes):
            min_ops = 0
            for j in ones:
                if i != j:
                    min_ops += abs(i-j)

            ans[i] = min_ops



        return ans