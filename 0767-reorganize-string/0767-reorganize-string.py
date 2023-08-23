class Solution:
    def reorganizeString(self, s: str) -> str:
        # refrred from : https://leetcode.com/problems/reorganize-string/discuss/3948675/Detailed-C%2B%2B-Solution-or-O(N)-or-Without-Heap-or-Beats-100-in-Time
        
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        n = len(s)
        

        print(s)
        
        if n == 1:
            return s
        
        s = list(s)
        
        i = 0
        j = 1
        
        # In summary, the flag is used to indicate whether the initial 
        # reorganization was successful or not. If not, it triggers a 
        # reverse of the string and another attempt to reorganize it. 
        # If even that attempt fails, an empty string is returned to 
        # signify that reorganization is not possible.
        flag = False
        
        # Initial recognition
        while j<n:
            
            if s[i] == s[j]:
                i = j
                while j<n and s[i]==s[j]:
                    j += 1
                    
                if j == n:
                    flag = True
                    continue
                    
                swap(s,i,j)
                
            i += 1
            j = i + 1
            
        
        # another attempt as flag is set true
        if flag:
            # reverse string
            s = s[::-1]
            
            i = 0
            j = i + 1

            while j<n:

                if s[i] == s[j]:
                    i = j
                    while s[i]==s[j]:
                        
                        j += 1
                        
                        if j == n:
                            return ""
                    
                    swap(s,i,j)

                i += 1
                j = i + 1
            
            
            
        
        
        return "".join(s)