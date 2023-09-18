class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        row_num_soldier_count = []
        for i,val in enumerate(mat):
            row_num_soldier_count.append( (i,val.count(1)) )
            
        #print(f'{row_num_soldier_count}')

        row_num_soldier_count.sort(key=lambda x:x[1])
        
        #print(f'sorted : {row_num_soldier_count}')
        
        return [x[0] for x in row_num_soldier_count][:k]