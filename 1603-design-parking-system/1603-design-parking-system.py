class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        
        #check carType big 1
        if carType == 1:
            # it is big carType
            # check slot is available
            if self.big >= 1:
                # allocate parking and update slots
                self.big -= 1
                return True
                
        
        #medium 2
        #check carType medium 2
        if carType == 2:
            # it is medium carType
            # check slot is available
            if self.medium >= 1:
                # allocate parking and update slots
                self.medium -= 1
                return True
                
        #small 3
        #check carType small 3
        if carType == 3:
            # it is big carType
            # check slot is available
            if self.small >= 1:
                # allocate parking and update slots
                self.small -= 1
                return True
            
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)