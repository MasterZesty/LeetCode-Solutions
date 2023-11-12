 ## Intuition/Approch

1. we have given a array of bus routes where routes[i] represents ith bus
takes.
2. now we want to go from a source to target by taking min number of buses
3. initially we are not on the bus


* as per constraints there are 500 buses

#### Approch 1:  Using Buses as nodes and using Dijkstra
```

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        ios_base::sync_with_stdio(false);
        if(source==target) return 0;
        unordered_map<int,vector<int>>mp;
        for(int i=0;i<routes.size();i++){
            for(int j=0;j<routes[i].size();j++){
                mp[routes[i][j]].push_back(i);
            }
        }
        unordered_map<int,vector<int>>mp1;
        for(auto &it:mp){
            for(int i=0;i<it.second.size();i++){
                for(int j=i+1;j<it.second.size();j++){
                    mp1[it.second[i]].push_back(it.second[j]);
                    mp1[it.second[j]].push_back(it.second[i]);
                }
            }
        }
        int ans=INT_MAX;
        vector<int> path(routes.size(), INT_MAX); 
        priority_queue<pair<int, int>> q;
       for(auto &it:mp[source]){ 
        path[it] = 0;
        q.push({ path[it], it });
       }
        while (!q.empty()) {
            auto it = q.top();
            q.pop();
            int parent = it.second;
            int cost = it.first;
            for (auto &x : mp1[parent]) {
                if (1 + cost < path[x]) {
                    path[x] = 1 + cost;
                    q.push({ path[x], x });
                }
            }
        }
        for(int i=0;i<mp[target].size();i++){
            ans=min(ans,path[mp[target][i]]);
        }
       if(ans==INT_MAX) return -1;
       return ans+1;
    }
};
```


* https://leetcode.com/problems/bus-routes/discuss/4277892/Beats-100-Explained-With-Video-Modified-Bellman-Ford-Visualized-Too
* https://leetcode.com/problems/bus-routes/discuss/4278651/Easy-Solution-Full-Explanation-oror-Ex-Uber-question-oror-Dijkstra


#### Approch 2:
* https://leetcode.com/problems/bus-routes/discuss/4277892/Beats-100-Explained-With-Video-Modified-Bellman-Ford-Visualized-Too

```
class Solution(object):
    def numBusesToDestination(self, routes, source, target):
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

```
