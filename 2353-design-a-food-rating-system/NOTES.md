### Attempt 1:
​
```python
class FoodRatings:
​
def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
self.food_cuisine = {}
self.cuisine_food_rating = {}
self.food_rating = {}
for food, cuisine, rating in zip(foods, cuisines, ratings):
# maintain food data at cuisine level cuisine/food_name/rating
self.cuisine_food_rating[cuisine] = self.cuisine_food_rating.get(cuisine,[]) + [(food, rating)]
# maintain food vs cuisine for lookup
self.food_cuisine[food] = cuisine
self.food_rating[food] = rating
​
# print(f"{self.cuisine_food_rating} \n {self.food_cuisine} \n {self.food_rating} ")
​
def changeRating(self, food: str, newRating: int) -> None:
old_food_rating = (food,self.food_rating[food])
self.food_rating[food] = newRating
self.cuisine_food_rating[ self.food_cuisine[food] ].remove(old_food_rating)
self.cuisine_food_rating[ self.food_cuisine[food] ] += [(food,newRating)]
# print()
# print(f"{self.cuisine_food_rating} \n {self.food_cuisine} \n {self.food_rating} ")
​
def highestRated(self, cuisine: str) -> str:
return sorted( self.cuisine_food_rating[cuisine], key = lambda x: ( -x[1], x[0] ) )[0][0]
​
​
# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
```
​
​