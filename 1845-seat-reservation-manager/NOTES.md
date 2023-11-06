## TLE Error

```
class SeatManager:

    def __init__(self, n: int):
        self.seat_status = ["unreserve"]*n
        

    def reserve(self) -> int:
        #print(f'reserve in process : {self.seat_status}')
        i = 0
        n = len(self.seat_status)
        while i < n:
            if self.seat_status[i] == "unreserve":
                self.seat_status[i] = "reserve"
                #print(f'reserve! sucess! : {self.seat_status}')
                return i + 1
            
            i += 1
            
        return -1
        

    def unreserve(self, seatNumber: int) -> None:
        #print(f'unreserved in process : {self.seat_status} seat : {seatNumber}')
        self.seat_status[seatNumber - 1] = "unreserve"
        #print(f'unreserved! success! : {self.seat_status} seat : {seatNumber}')
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```

## use python lib also gives TLE

```
class SeatManager:

    def __init__(self, n: int):
        self.seat_status = ["unreserve"]*n
        

    def reserve(self) -> int:
        #print(f'reserve in process : {self.seat_status}')
        i = self.seat_status.index("unreserve")
        self.seat_status[i] = "reserve"
        return i + 1
        

    def unreserve(self, seatNumber: int) -> None:
        #print(f'unreserved in process : {self.seat_status} seat : {seatNumber}')
        self.seat_status[seatNumber - 1] = "unreserve"
        #print(f'unreserved! success! : {self.seat_status} seat : {seatNumber}')
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```

## Approch 3 - Gives TLE

```
class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.next_seat = 1
        self.reserved_seats = []

    def reserve(self) -> int:
        self.reserved_seats.append(self.next_seat)
        reserved_seat = self.next_seat
        
        while self.next_seat <= self.n:
            if self.next_seat not in self.reserved_seats:
                break
            self.next_seat += 1
            
        return reserved_seat

    def unreserve(self, seatNumber: int) -> None:
        if self.next_seat > seatNumber:
            self.next_seat = seatNumber
        
        self.reserved_seats.remove(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```

### Read about  priority queue (min-heap) 
https://docs.python.org/3/library/heapq.html

```
class SeatManager:
    def __init__(self, n):
        self.seats = []  # Initialize an empty list to manage seat reservations.
        self.n = n

        # Initialize the list with seat numbers from 1 to 'n'.
        for i in range(1, n + 1):
            heapq.heappush(self.seats, i)

    # Reserve a seat.
    def reserve(self):
        if self.seats:  # Check if there are available seats in the list.
            reserved_seat = heapq.heappop(self.seats)  # Get the smallest seat number from the list.
            return reserved_seat  # Return the reserved seat number.
        else:
            return -1  # Return -1 to indicate that there are no available seats.

    # Unreserve a seat.
    def unreserve(self, seat_number):
        if 1 <= seat_number <= self.n:
            heapq.heappush(self.seats, seat_number)  # Add the unreserved seat back to the list.
```
