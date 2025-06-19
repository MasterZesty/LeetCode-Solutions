class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        '''
        HINT 1 : Which values in each subsequence matter? The only values that matter are the maximum and minimum values.
        HINT 2 : Let the maximum and minimum values of a subsequence be Max and Min. It is optimal to place all values in between Max and Min in the original array in the same subsequence as Max and Min.
        '''
        
        min_num_subseq = 0
        # min_num_subseq === number of transitions to new groups
        # min_num_subseq + 1 === total number of groups

        nums_sorted = sorted(nums)

        # print(nums, nums_sorted)

        i = 0
        j = 0
        n = len(nums)

        # as array is sorted we will start with finding first subsequence
        while i < n and j < n:

            # max - min
            if nums_sorted[j] - nums_sorted[i] <= k:
                j += 1 # increse the subseq

            else:
                # end subseq and start new one
                i = j
                min_num_subseq += 1


        
        return min_num_subseq + 1 # +1 needed because min-num_seq only increse when new group starts