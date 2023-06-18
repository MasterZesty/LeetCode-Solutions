class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # ref : https://youtu.be/k5GjTnkECHc
        # https://leetcode.com/problems/make-array-strictly-increasing/discuss/3646689/Java-oror-C%2B%2B-ororPython-oror-Solution-Easy-To-Understand
        arr2 = sorted(arr2)
        dict_pre = {0: -float("inf")}
		
        for num in arr1:
            dict_cur = collections.defaultdict(lambda: float("inf"))
            for n_swap in dict_pre:
                if num > dict_pre[n_swap]:
                    dict_cur[n_swap] = min(dict_cur[n_swap], num)
                loc = bisect.bisect(arr2, dict_pre[n_swap])
                if loc < len(arr2):
                    dict_cur[n_swap+1] = min(dict_cur[n_swap+1], arr2[loc])
                    
            if not dict_cur:
                return -1
            dict_pre = dict_cur
            
        return min(dict_pre.keys())