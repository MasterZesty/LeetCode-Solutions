class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        n = len(dist)
        # find time when each monter arrives at city as we want to eliinate
        # a monter who arrives first
        arrival_time_to_city = [dist[i]/speed[i] for i in range(n)]
        
        # sort the time array 
        sorted_arrival_time_to_city = sorted(arrival_time_to_city)
        
        #simulate the game - process of eliminating monsters one by one
        for i in range(n):
            
            if sorted_arrival_time_to_city[i] <= i:
                return i
        
        
        
        return n