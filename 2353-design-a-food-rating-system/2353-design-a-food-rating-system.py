class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.cuisine_to_heap = defaultdict(list)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (food, cuisine, -rating)
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        food, cuisine, old_rating = self.food_info[food]
        self.food_info[food] = (food, cuisine, -newRating)
        
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:
        highest_rated_food = None
        
        while len(self.cuisine_to_heap[cuisine]) > 0:
            curr = self.cuisine_to_heap[cuisine][0]
            if curr[0] != self.food_info[curr[1]][2]:
                heapq.heappop(self.cuisine_to_heap[cuisine])
                continue
            highest_rated_food = curr[1]
            break
        return highest_rated_food

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)