class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        # A permutation also called an “arrangement number” or “order,” is 
        # a rearrangement of the elements of an array, arr into a one-to-one 
        # correspondence with arr itself. An array of length n has n! Permutation.
        
        # Approch 1 _ TLE + Memory LE
        
#         def helper_is_ap(arr):
#             d = abs(arr[0]-arr[1])
#             l = len(arr)
#             # print(f'a: {arr} d :{d} l: {l}')

#             if l == 2:
#                 return True

#             for i,v in enumerate(arr):

#                 if i != l-1:

#                     if abs(arr[i]-arr[i+1]) !=  d:
#                         return False


#             return True
        
#         import itertools
#         permutations = (itertools.permutations(arr))
        
#         for permutation in permutations:
#             if helper_is_ap(permutation):
#                 # print(f'AP Sequnce: {permutation}')
#                 return True
            
#         return False

        # Approch 2

        arr.sort()  
        diff = arr[1] - arr[0]

        
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False

        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        