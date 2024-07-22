class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        zipped = zip(names, heights)
        
        s = sorted(zipped, key=lambda x:x[1], reverse=True)
        
        n, h = zip(*s)
        
        # print(n,h,s)
        
        return list(n)