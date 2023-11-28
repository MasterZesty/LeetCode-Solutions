class Solution:
    def numberOfWays(self, corridor: str) -> int:
        
        MOD = 10**9 + 7
        
        no_of_seats = corridor.count("S")
        
        if no_of_seats == 0:
            return 0
        
        if no_of_seats % 2 != 0:
            return 0
        
        seat_group = [[-1,-1] for _ in range(no_of_seats//2)]
        
        # print(f'no_of_seats {no_of_seats} | seat_group {seat_group}')
        
        s = 0
        first_flag = False
        second_flag = True
        for i,c in enumerate(corridor):
            
            if c == "S" and not second_flag:
                seat_group[s][1] = i
                second_flag = True
                first_flag = False
                # print(f'i {i} c {c} s {s} seat_group {seat_group}')
                s += 1
                continue
            
            if c == "S" and not first_flag:
                seat_group[s][0] = i
                first_flag = True
                second_flag = False
                
            # print(f'i {i} c {c} s {s} seat_group {seat_group}')
                
        # print(f'no_of_seats {no_of_seats} | seat_group {seat_group}')
        
        if len(seat_group) == 1:
            return 1
        
        max_ways_to_divide_corridor = 1
        
        
        for j in range(0,len(seat_group)-1):
            # print(f'group {seat_group[j]} possibel ways {( seat_group[j+1][0] - seat_group[j][1])}')
            max_ways_to_divide_corridor *= ( seat_group[j+1][0] - seat_group[j][1])
            
        # print(f'max_ways_to_divide_corridor {max_ways_to_divide_corridor}')
            
        
        
        return max_ways_to_divide_corridor % MOD