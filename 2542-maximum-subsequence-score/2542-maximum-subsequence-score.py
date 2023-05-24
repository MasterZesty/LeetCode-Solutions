class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """ Approch 1 : gives TLE error!!!!!!
        
        # we will first generate num1 subsequnces with some efficent method
        # and in that same methods we will select same index as of num1 for num2
        # and then compare min in num2 sequnece.
        # here important is to generate subsequnce with efficiency
        
        def subseq(nums,binary,n):
            # nums - nums array
            # binary - binary represenatation
            # n - length of array
            
            sub = []
            
            for j in range(n):
                
                # check if any bit set to 1
                # 1<<j --> The bitwise shift operation (1 << j) shifts the 
                #          binary representation of 1 (which is 0001) by j positions to the left
                #
                # bitwise AND operation binary & (1 << j) compares the corresponding bits of binary and 1 << j.
                
                if (binary & (1<<j)):
                    sub.append(nums[j])
                    
                    
            return sub
        
        count = -1
        
        n = len(nums1)
        
        # total no of non-empty subseq 2^n -1 
        limit = 2**n

        for i in range(1, limit):
            # Generate subsequence for binary i
            sub = subseq(nums1, i, n)
            
            if len(sub) == k:
                sub2 = subseq(nums2, i, n)
                
                # Calculate the sum and minimum value for sub and sub2
                temp_sum = sum(sub)
                temp_min = min(sub2)
                
                temp_count = temp_sum * temp_min
                
                # Update count if the current count is smaller
                if temp_count > count:
                    count = temp_count
                    
        return count
    
        # The time complexity of your code is O(2^n * n), where n is the length of `nums1`. 
        # This complexity arises from generating all possible subsequences using the binary 
        # representation (2^n) and the inner loop that iterates over the elements of `nums1` (n).
        
        ------------------------------------------------------------------------------------------"""
        
        # Aprroch 2: ref : https://leetcode.com/problems/maximum-subsequence-score/discuss/3082942/Python-3Sort-and-visit-set
        
        # goes from smallest to largest for nums2
        n2 = sorted((x, i) for i, x in enumerate(nums2))
        
        # pick the largest from nums1
        n1 = sorted([(x, i) for i, x in enumerate(nums1)], key=lambda x: (-x[0], x[1]))
        
        # visited index
        vis = set()
        
        # running total, final answer and length of queue
        tot = ans = cnt = 0
        # pointer for n2
        j = 0
        
        # for current minimum from nums2
        for x, i in n2:
            # if not visited, add to the running total
            if i not in vis: 
                vis.add(i)
                cnt += 1
                tot += nums1[i]
                
            # if length of queue < k, select the largest from nums1
            while j < len(n1) and cnt < k:
                a, b = n1[j]
                if b not in vis:
                    tot += a
                    cnt += 1
                    vis.add(b)
                j += 1
            
            # once length == k, updates the final answer and take out current num from nums2
            if cnt == k:
                ans = max(ans, x * tot)
                cnt -= 1
                tot -= nums1[i]
            if j == len(n1): return ans
            
        return ans
