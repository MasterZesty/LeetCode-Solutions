class Solution:
    def minSteps(self, s: str, t: str) -> int:
        shmap = {}
        thmap = {}
        
        ns = len(s)
        nt = len(t)
        
        for i in range(ns):
            shmap[s[i]] = shmap.get(s[i],0) + 1
            
        for i in range(nt):
            thmap[t[i]] = thmap.get(t[i],0) + 1
            
            
        min_steps = 0
        print(f"s: {shmap} \n t: {thmap}")
        
        for char,count in shmap.items():
            if thmap.get(char, 0) == 0:
                print(f"char: {char} | add count: {count}")
                min_steps += count
            
            elif thmap.get(char, 0) != 0:
                s_count = count
                t_count = thmap[char]
                
                if s_count > t_count:
                    c = (s_count - t_count)
                    
                    print(f"char: {char} | add count: {c}")
                    min_steps += c
                    
            print(f"min_steps: {min_steps}")
                
        return min_steps