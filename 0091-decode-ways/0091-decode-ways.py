class Solution:
    def numDecodings(self, s: str) -> int:
        
        def decode_num(encoded_s: str, memo={}):
            if not encoded_s:
                return 1
            
            if encoded_s in memo:
                return memo[encoded_s]
            
            ways = 0
            if encoded_s[0] != '0':
                ways += decode_num(encoded_s[1:], memo)
                
                if len(encoded_s) >= 2 and 1 <= int(encoded_s[:2]) <= 26:
                    ways += decode_num(encoded_s[2:], memo)
            
            memo[encoded_s] = ways
            return ways
        
        return decode_num(s)
