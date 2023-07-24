class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # each palindrome have L part + M part + R part
        # ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
        
        hmap = {}
        used = []
        
        for i,word in enumerate(words):
            if word not in hmap.keys():
                hmap[word] = 1
                
            else:
                hmap[word] += 1
                
        print(hmap)
        
        ans = 0
        flag = True
        
        for i in range(len(words)):
            # 2 cases
            s = words[i]

            # case 1 s[0] != s[1]
            if s[0] != s[1]:
                if hmap.get(s[::-1],0) != 0:
                    t =  min(hmap.get(s,0),hmap.get(s[::-1],0))
                    del hmap[s]
                    del hmap[s[::-1]]
                    
                    ans += t*4
                    
            # case 2 s[0] == s[1]
            if s[0] == s[1]:
                print(ans)
                t = hmap.get(s,0)
                if t != 0:
                    if t%2 == 0: # EVEN
                        ans += t*2
                    else: # ODD
                        # occuring odd number of times
                        if flag:
                            ans += t*2
                            flag = False

                        else:
                            ans += (t-1)*2
                    del hmap[s]
        print(hmap,flag)        
        return ans