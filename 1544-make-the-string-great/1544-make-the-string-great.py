class Solution:
    def makeGood(self, s: str) -> str:
        
        def makeGood_helper(s,ref):
            
            print('Main string: ',s)
            
            if s=='' or (s.islower()) or (s.isupper()) or len(s) <= 2:
                
                if len(s) == 1:
                    return s
                
                if len(s) == 2:
                    # print('len <= 2')
                    # case 1 aA
                    # case 2 Aa
                    # case 3 a
                    # case 4 A
                    
                    
                    # s[0] = upper and s[1] = lower
                    if (ord(s[0]) >= 65 and ord(s[0]) <=90) and (ord(s[1]) >= 97 and ord(s[1])<=122):
                        if (chr(ord(s[0])-ord('A')) == chr(ord(s[1])-ord('a'))):
                            return ''
                    # s[0] = lower and s[1] = upper   
                    if (ord(s[1]) >= 65 and ord(s[1]) <=90) and (ord(s[0]) >= 97 and ord(s[0])<=122):
                        if (chr(ord(s[0])-ord('a')) == chr(ord(s[1])-ord('A'))):
                            return ''
                        
                return s
            else:
                
                temp = s

                for i in range(len(s)-1):

                    s_A = ord('A')
                    s_a = ord('a')

                    s_current = ord(s[i])
                    s_next  = ord(s[i+1])

                    # case 1 curr=>uppar : next=>lower same charecter

                    f_current_uppar = (s_current >= 65 and s_current<=90)
                    f_next_lower = (s_next >= 97 and s_next<=122)

                    flag_c1 = f_current_uppar and f_next_lower


                    # check Uppar-case and lower case
                    if (flag_c1):
                        if (chr(s_current-s_A) == chr(s_next-s_a)):
                            # print('string: ',s[:i],s[i+2:])
                            temp = s[:i] + s[i+2:]
                            # print('temp1: ',temp)


                    # case 2 curr=>low : next=>Uppar same charecter

                    f_current_lower = (s_current >= 97 and s_current<=122)
                    f_next_uppar = (s_next >= 65 and s_next<=90)

                    flag_c2 = f_current_lower and f_next_uppar

                    if (flag_c2):
                        if( chr(s_current-s_a) == chr(s_next-s_A)):
                            # print('string2: ',s[:i],s[i+2:])
                            temp = s[:i] + s[i+2:]
                            # print('temp2: ',temp)

                print('temp:',temp)
                # s = makeGood_helper(temp)
                if temp == ref:
                    print('temp == ref  returning',temp)
                    return s
                ref = temp
                return makeGood_helper(temp,ref)
                
            
        return makeGood_helper(s,s)   

