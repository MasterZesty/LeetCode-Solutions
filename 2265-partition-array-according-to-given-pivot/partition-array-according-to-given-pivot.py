class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        from collections import deque

        q_low = deque()
        q_high = deque()
        q_equal = deque()

        for num in nums:

            if num < pivot:
                q_low.appendleft(num)

            if num > pivot:
                q_high.appendleft(num)

            if num == pivot:
                q_equal.appendleft(num)

        # print(f"q_low:{q_low}")

        ans = []
        while q_low:
            ans.append(q_low.pop())

        while q_equal:
            ans.append(q_equal.pop())

        while q_high:
            ans.append(q_high.pop())

        return ans