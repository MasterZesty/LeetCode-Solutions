class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # approch 1 : MLE Error
        '''
        ans = ''
        for char in s:
            if char.isnumeric():
                ans = ans*int(char)
            else:
                ans += char
                
        # print(ans)
        
        return ans[k-1]
        '''
        # approch 2: use str length to avoid unnesaary compute and memory
        total_length = 0
        for char in s:
            if char.isnumeric():
                total_length = total_length*int(char)
            else:
                total_length += 1
                
        # print(total_length)
        
        # Start from the end of the string and work backward to find the kth character
        for char in reversed(s):
            if char.isnumeric():
                total_length //= int(char)
                k %= total_length
            else:
                if k == 0 or k == total_length:
                    return char
                total_length -= 1

        return ""