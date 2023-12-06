https://leetcode.com/problems/maximum-number-of-removable-characters/discuss/2939727/C%2B%2B-oror-Binary-Search-oror-Easy-approach

### Approch 1 : some index/logical errors but logc is same
```python
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        l = 0
        r = len(removable) - 1
        ans = 0
        
        
        while l <= r:
            mid = l + (r-l)//2
            # print(f"l: {l} r: {r}  mid: {mid}")
            
            t = list(s)
            
            # remove chars put _ for not disturb indexs
            for i in range(mid+1):
                t[removable[i]] = '_'
                
            # print(f"temp arr : {t}") 
            
            # validate is subsequnce present in temp
            m = len(p)
            k = 0
            for i in range(len(s)):
                
                # print(f"is subseq : {i} {t[i]} | k : {k} {p[k]}")
                
                if t[i] == p[k]:
                    k += 1
                
                if k >= m:
                    break
            
            # print(f"k {k} m {m}")        
            
            if k == m:
                # print(f"subsequence found ! moving to right | curr mid : {mid}")
                ans = mid
                l = mid + 1
                
            else:
                # print(f"subsequence not found ! moving to left | curr mid : {mid}")
                r = mid - 1
                
        return ans
```
