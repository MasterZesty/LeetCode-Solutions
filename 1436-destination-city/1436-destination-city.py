class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        n = len(paths)
        
        start_city = paths[0][0]
        destination_city = paths[0][1]
        
        start_cities = {}
        end_cities = {}
        
        for i, city in enumerate(paths):
            start_cities[city[0]] = 1
            end_cities[city[1]] = 1
            
        
        # print(f"start: {start_cities} | end: {end_cities}")
        
        for city in end_cities:
            if start_cities.get(city,0) == 0 and city != start_city:
                return city
            
        return destination_city