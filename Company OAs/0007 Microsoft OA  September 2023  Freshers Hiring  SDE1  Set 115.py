'''

ref: https://drive.google.com/file/d/1c63h3JmuhrwjAFXWS5Qw1fNfOaIClBQj/view
qlink: https://www.desiqna.in/15920/microsoft-oa-september-2023-freshers-hiring-sde1-set-115

*** Microsoft OA | September 2023 | Freshers Hiring | SDE1 | Set 115 ***

Challenge 1 description

A patient needs rehabilitation within the next N days (numbered from O to N-1). The
rehabilitation consists of X sessions. For every rehabilitation session, other than the
last one, the next session is exactly Y days later.

You are given an array A of N integers listing the costs of the individual rehabilitation
sessions on the N days: that is rehabilitation on the K-th day costs A[KJ.

Write a function:
int solution(int A[], int N, int X, int Y);

that, given the array A and the two integers X and Y, retums the minimum of
rehabilitation.

It is guaranteed that it is always possible to cornplete all X rehabilitation sæsions.

1. Given A = [4, 2, 3, 7], X = 2 and Y = 2, function should return 7, which is the sum
of the costs on days O and 2 (7 = 4 + 3).

2. Given A = [10, 3, 4, 7], X = 2 and Y = 3, your function should retum 17
rehabilitation is psible only on days O and 3 (17 = 10 + 7).

3. Given A = [4, 2, 5, 4, 3, 5, 1, 4, 2, 7], X = 3 Y = 2, your functim should return 6
which is the sum of the costs on days 4, 6 and 8 (6 = 3 + 1 + 2).

***  Solution/Approch  ***

we are given an array of size n. we have to
pick x elements at exactly y distance; sum of
them should be minimum.

## Apporch 1 : Brute force

ans = floor('inf')
for i in range(n):

    j = i # start at i index and jumps - to y distnace
    sum = 0 # stores sum for that iteration
    c = 0 #to keep track of jumps we need to jump exactly x times

    while ( j >= 1 and c < x):
        sum += A[j]
        c += 1
        j -= y #jump to y distnace

    if c==x:
        ans = min(ans,sum)

return ans

TC : O(n^2)
SC : O(1)

## Approch 2 : Prefix array/ precomputeation

prefix[i] = b[i - 0y] + b[i - 1y] + b[i -2y] +  ..... b[]

prefix[i] = b[i] + prefix[i - y]

ans[i] = prefix[i] - prefix[i - x*y] -> sum of x numbers from index i at distnace y

final ans => min(ans[0],ams[1],ans[2],....ans[i])

TC : O(n)
SP : O(1)

'''

a = [0,4, 2, 3, 7] # array start at index 1
x = 2
y = 2


n = 4

pref = [0 for i in range(n+1)]

# make prefix array
for i in range(1,n+1):
    if i-y >= 1:
        pref[i] = a[i] + pref[i -y]
    else:
        pref[i] = a[i]

print(f'given array : {a}')
print(f'prefix array : {pref}')

# calculate min cost
min_cost = float('inf')

for i in range(1,n+1):

    index = i - ( (x-1) *y)
    if index >= 1:
        g = pref[i]
        if index - y >= 1:
            g = g - pref[index - y]

        min_cost = min(g,min_cost)

print(f'min cost : {min_cost}')