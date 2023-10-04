class MyHashMap:

    def __init__(self):
        self.key = []
        self.val = []
        

    def put(self, key: int, value: int) -> None:
        try:
            # key already exists in the map, update the corresponding value
            index = self.key.index(key)
            self.val[index] = value
            
        except ValueError as err:
            
            # if not then insert
            self.key.append(key)
            self.val.append(value)

    def get(self, key: int) -> int:
        try:
            # key exists in the map, return value
            index = self.key.index(key)
            return self.val[index]
        
        except ValueError as err:
            # if not then
            return -1     

    def remove(self, key: int) -> None:
        try:
            # key exists in the map, return value
            index = self.key.index(key)
            self.key.pop(index)
            self.val.pop(index)
            
        except ValueError as err:
            
            # if not then
            return -1     


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)