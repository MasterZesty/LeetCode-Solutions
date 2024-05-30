class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        
        """
        Approch : https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/discuss/623747/JavaC%2B%2BPython-One-Pass-O(N4)-to-O(N)
        
        a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
        b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

        Assume a == b, thus
        a ^ a = b ^ a, thus
        0 = b ^ a, thus
        arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0
        prefix[k+1] = prefix[i]

        We only need to find out how many pair (i, k) of prefix value are equal.
        So we can calculate the prefix array first,
        then brute force count the pair.

        Because we once we determine the pair (i,k),
        j can be any number that i < j <= k,
        so we need to plus k - i - 1 to the result res.

        Time O(N^2)
        Space O(N)
        Space O(1) if changing the input
        
        """
#         A = arr
#         A.insert(0, 0)
        
#         n = len(A)
#         for i in range(n - 1):
#             A[i + 1] ^= A[i]
#         res = 0
#         print(A)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if A[i] == A[j]:
#                     res += j - i - 1
#         return res
        
        m = len(arr)
        prefix = [arr[i] for i in range(m)]
        prefix.insert(0,0)
        n = len(prefix)
        
        for i in range(n-1):
            prefix[i+1] ^= prefix[i]
            
        
        # print(f"prefix: {prefix}")
        
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                
                if prefix[i] == prefix[j]:
                    
                    count += j - i - 1
        
        return count
