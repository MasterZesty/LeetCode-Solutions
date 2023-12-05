## Approch 1 : TLE
```python
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        '''
        intialize an array with given input arr
        '''
        self.arr = arr
        

    def query(self, left: int, right: int, value: int) -> int:
        '''
        use binary search to find given elemnt and then
        do not stop at break condition perform till we scanned the array
        '''
        sub_arr = self.arr[left:right+1]
        
        # sort the arr
        sub_arr.sort()
        
        count = 0
        
        # print(f"arr is : {sub_arr}")
        
        l = 0
        r = len(sub_arr) - 1
        n = len(sub_arr) - 1
        
        while l <= r:
            
            mid = l + (r - l)//2
            
            # print(f"l: {l} r: {r} mid: {mid} arr value: {sub_arr[mid]} | search arr {sub_arr[l:r+1]}")
            
            if sub_arr[mid] == value:
                count += 1
                
                # Expand the search space
                
                # to left
                i = mid - 1
                while i >= 0 and sub_arr[i] == value:
                    count += 1
                    i -= 1
                
                # to right
                i = mid + 1
                while i <= n and sub_arr[i] == value:
                    count += 1
                    i += 1
                
                # break this because we found all occrnaces of values
                # we can not expand this window further
                break

            if sub_arr[mid] > value:
                r = mid - 1
            
            if sub_arr[mid] < value:
                l = mid + 1

                
            # print(f"l: {l} r: {r} mid: {mid} arr value: {sub_arr[mid]} | search arr {sub_arr[l:r+1]}")
        
        # print(f"count {value} is {count}")
        return count


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
```
