import bisect

class RangeFreqQuery:
    '''
    Important Bisection Functions 
    
    1. bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument 
                                    can be placed so as to maintain the resultant list in sorted order. If the element is already present 
                                    in the list, the rightmost position where element has to be inserted is returned.

    This function takes 4 arguments, list which has to be worked with, a number to insert, starting position in list to consider, ending position which has to be considered. 

    2. bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be 
                                            placed so as to maintain the resultant list in sorted order. If the element is already present in the 
                                            list, the leftmost position where element has to be inserted is returned. 

    This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered. 

    3. bisect_right(list, num, beg, end) :- This function works similar to the “bisect()” and mentioned above. 
    
    '''
    
    def __init__(self, arr):
        self.hm = {i: [] for i in arr}
        for index, value in enumerate(arr):
            self.hm[value].append(index)
        
        # Ensuring the lists remain sorted
        for key in self.hm:
            self.hm[key].sort()

        # print(f"data structure is value: [i1, i2, ...] {self.hm}")


    def query(self, left, right, value):
        
        if value not in self.hm:
            return 0
        
        subarr = self.hm[value]
        
        l = bisect.bisect_left(subarr, left)
        r = bisect.bisect_right(subarr, right)
        
        return r - l

        
        

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
