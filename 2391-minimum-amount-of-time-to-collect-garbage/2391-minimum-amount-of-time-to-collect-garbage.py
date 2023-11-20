class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        n_house = len(garbage) 
        
        # minimum number of minutes needed to pick up all the garbage
        min_time = 0
        
        # three garbage trucks
        
        time_required_to_reach_house = [0]*n_house
        
        for i in range(1,n_house):
            time_required_to_reach_house[i] += time_required_to_reach_house[i-1] + travel[i-1]
            
        # print(f'time_required_to_reach_house : {time_required_to_reach_house}')
        
        # handle case when there is no G P M or all G or M or P are colleted
        # this is for when we collect all garbage we no longer need to move trucks
        # as demostrated in testcases
        i_last_occurance_M = -1
        i_last_occurance_G = -1
        i_last_occurance_P = -1
        
        for i in range(n_house):
            
            if "M" in garbage[i]:
                i_last_occurance_M = i
            
            if "G" in garbage[i]:
                i_last_occurance_G = i
            
            
            if "P" in garbage[i]:
                i_last_occurance_P = i

        # print(f'i_last_occurance_M {i_last_occurance_M} | i_last_occurance_G {i_last_occurance_G} | i_last_occurance_P {i_last_occurance_P}')
            
            
        # let us count time required to collect glass for truck G
        t_GTruck = 0
        
        time_required_to_reach_prev_house = 0
        
        if i_last_occurance_G != -1:
            # collect garbage
            for i,s in enumerate(garbage):
                
                if i_last_occurance_G + 1 == i:
                    break

                t_to_reach_house = time_required_to_reach_house[i] - time_required_to_reach_prev_house
                time_required_to_reach_prev_house = time_required_to_reach_house[i]

                # only consider glass
                t_to_pick_garbage = s.count("G")

                t_GTruck += t_to_reach_house + t_to_pick_garbage

                # print(f'Glass Truck at house {i} | t_to_pick_garbage {t_to_pick_garbage} | t_to_reach_house {t_to_reach_house}')
        
        # print(f'time required for Glass truck : {t_GTruck}')
        
        
        
        # let us count time required to collect paper for truck P
        t_PTruck = 0
        
        time_required_to_reach_prev_house = 0
        
        if i_last_occurance_P != -1:
            # collect garbage
            for i,s in enumerate(garbage):
                
                if i_last_occurance_P + 1 == i:
                    break

                t_to_reach_house = time_required_to_reach_house[i] - time_required_to_reach_prev_house
                time_required_to_reach_prev_house = time_required_to_reach_house[i]

                # only consider glass
                t_to_pick_garbage = s.count("P")

                t_PTruck += t_to_reach_house + t_to_pick_garbage

                # print(f'Paper Truck at house {i} | t_to_pick_garbage {t_to_pick_garbage} | t_to_reach_house {t_to_reach_house}')
        
        # print(f'time required for Paper truck : {t_PTruck}')
        
        
        
        
        # let us count time required to collect Metal for truck M
        t_MTruck = 0
        
        time_required_to_reach_prev_house = 0
        
        if i_last_occurance_M != -1:
            # collect garbage
            for i,s in enumerate(garbage):
                
                if i_last_occurance_M + 1 == i:
                    break

                t_to_reach_house = time_required_to_reach_house[i] - time_required_to_reach_prev_house
                time_required_to_reach_prev_house = time_required_to_reach_house[i]

                # only consider glass
                t_to_pick_garbage = s.count("M")

                t_MTruck += t_to_reach_house + t_to_pick_garbage

                # print(f'Metal Truck at house {i} | t_to_pick_garbage {t_to_pick_garbage} | t_to_reach_house {t_to_reach_house}')

        # print(f'time required for Metal truck : {t_MTruck}')
            
        min_time = t_MTruck + t_PTruck + t_GTruck
        
        return min_time