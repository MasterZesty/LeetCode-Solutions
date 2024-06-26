class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        '''
        ref : https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/239284/C%2B%2B-greedy-stack-and-O(1)-memory
        '''
        
        # Aproch 1:
        '''
        res = 0
        
        n = len(nums)
        
        for  i in range(n):
            
            if nums[i] != 1:
                
                if i+k-1 >= n:
                    return -1
                
                for j in range(i, i+k):
                    nums[j] = 1 - nums[j]
                
                res += 1
                
                
        return res
        '''
        
        # Aproch 2:
        '''
        ref - https://youtu.be/Y6ZrtZgmwRg?si=e9y1w073MEEvAlWh
        '''
        ''''
        n = len(nums)
        flips = 0
        
        flip = [False]*n
        current = 0
        for i,x in enumerate(nums):
            
            if flip[i]:
                current ^= 1
            
            if (x^current) == 0:
                
                flips += 1
                current ^= 1
                
                
                if i+k > n:
                    return -1
                
                if i+k < n:
                    flip[i+k] = True
                

                
        
        return flips
        '''
        # Aproch 3
        '''
        ref - https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/238538/Python-O(n)-using-queue-and-how-to-get-rid-of-the-queue
        '''
        
        from collections import deque
        
        q = deque()
        res = 0
        for i in range(len(nums)):
        
            if len(q) % 2 != 0:
                if nums[i] == 1:
                    res += 1
                    q.append(i+k-1)
            else:
                if nums[i] == 0:
                    res += 1
                    q.append(i+k-1)
            if q and q[0] == i: q.popleft()
            if q and q[-1] >= len(nums): return -1
        return res
