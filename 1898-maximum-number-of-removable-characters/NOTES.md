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