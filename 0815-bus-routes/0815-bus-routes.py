class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        # ref :https://leetcode.com/problems/bus-routes/discuss/4277892/Beats-100-Explained-With-Video-Modified-Bellman-Ford-Visualized-Too
        # TC : 
        '''
        Complexity
Time Complexity:

The outer loop runs until no more updates can be made, and in each iteration, we iterate through all routes. Therefore, the time complexity is O(n * m), where n is the number of routes and m is the average number of stops in a route.
Space Complexity:

The space complexity is O(maxStop), where maxStop is the maximum bus stop number in any route, as we use an array minBusesToReach of this size
'''
        if source == target:
            return 0

        max_stop = max(max(route) for route in routes)
        if max_stop < target:
            return -1

        n = len(routes)
        min_buses_to_reach = [float('inf')] * (max_stop + 1)
        min_buses_to_reach[source] = 0

        flag = True
        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, min_buses_to_reach[stop])
                mini += 1
                for stop in route:
                    if min_buses_to_reach[stop] > mini:
                        min_buses_to_reach[stop] = mini
                        flag = True

        return min_buses_to_reach[target] if min_buses_to_reach[target] < float('inf') else -1