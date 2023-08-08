'''
In a fictional stock market, fund managers are required to create
portfolios by including stocks from different industries.

Given an array, stocks, where the stocks[i] represent the number
of companies in the ith industry. The task is to distribute stocks
in such a way that each portfolio has exactly k distinct types of
stocks where k is a given integer and each company is included only
once in a portfolio.

Find the maximum number of portfolios that can be created.

Input Format

- The first line contains an integer k, that represents the distinct kinds of stocks that each portfolio must have.
- The second line contains an integer n, that represents the different kinds of stocks.
- The next n lines represent stocks[i] that represent the count of stocks of the kind i

Example:
k=2, n=3, stocks = [3, 3, 3].
Each portfolio must have 2 kinds of stocks (as k = 2).
One of the optimal methods can be:
Portfolio 1 gets stocks of kinds 1 and 2.
Portfolio 2 gets stocks of kinds 1 and 3.
Portfolio 3 gets stocks of kinds 2 and 3. P
ortfolio 4 gets stocks of kinds 1 and 2.

It can be proved that no more than 4 portfolios can be created.
Hence the answer is 4.

Function Description

Complete the function getMaxPortfolios in the editor below. getMaxPortfolios has the following parameter(s):
k: An integer
stocks[n]. An array of integers
Returns
long. An integer that represents the maximum number of portfolios

Constraints
1 <= sk <= 10^5
1 <= ns <= 10^5
1 <= stocks[i] <= 10^9
'''


def check_y(y):
    # this function gets value
    # of Y i.e. is it possible
    # to make y groups of each
    # size k

    # sum = Y*K
    t  = y*k
    i = 0
    while i<n:
        
        if arr[i] > y:
            t -= y
        else:
            t -= arr[i]

        i += 1

    return t <= 0 

def getMaxPortfolios(n,k,arr):
    s = sum(arr)
    ans = -1

    # approch 1: bruteforce check all possible Y groups
    # TC - O(S*N) - sum*check function while loop

    # i = 1
    # while i <= s:  # y's value could maximum go to sum(arr elements)

    #     if check_y(i) == False:
    #         # since it will break after the last
    #         # possible group we are doing -1
    #         ans = i-1
    #         break
    #     else:
    #         i += 1

    # apporch 2: using binary serach limit range of search
    # TC - O(log(S)*N) - as we are limting range of search
    low = 1
    high = 10**18 # max possible value of stock[i] is 10^9 so sum = 10^9*10^9 = 10^18
    y = 0

    while low <= high and y == 0:
        mid = (low + high) // 2

        if check_y(mid) and not check_y(mid + 1):
            ans = mid
            y = 1
        elif check_y(mid):
            low = mid       # right.....
        else:
            high = mid - 1  # left......


    print(f'no of portfolio possible are : {ans}')

if __name__ == "__main__":
    k = 2
    arr = [3,3,3]
    n = len(arr)
    getMaxPortfolios(n,k,arr)

