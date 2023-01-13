class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s)
        
        for i in range(len(s)):
            
            # print(i,j,s[i],s[j-1],j//2)
            
            if (i == j) or (len(s)//2 == i):
                # print("breking",i,j)
                break
                
            s[i], s[j-1] = s[j-1], s[i]
            
            j -= 1
        