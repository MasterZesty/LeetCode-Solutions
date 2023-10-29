class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        
        tests_per_pig = minutesToTest // minutesToDie + 1
        pigs = 0
        #print(f'tests_per_pig {tests_per_pig} pigs {pigs} buckets {buckets}')
        
        while tests_per_pig**pigs < buckets:  # tests_per_pig**pigs => calculates the total number of tests that all the pigs can collectively perform
            pigs += 1
        
        return pigs