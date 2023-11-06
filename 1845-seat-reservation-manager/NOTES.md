​
def unreserve(self, seatNumber: int) -> None:
if self.next_seat > seatNumber:
self.next_seat = seatNumber
self.reserved_seats.remove(seatNumber)
​
​
# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
```
​
### Read about  priority queue (min-heap)
https://docs.python.org/3/library/heapq.html
​
```
class SeatManager:
def __init__(self, n):
self.seats = []  # Initialize an empty list to manage seat reservations.
self.n = n
​
# Initialize the list with seat numbers from 1 to 'n'.
for i in range(1, n + 1):
heapq.heappush(self.seats, i)
​
# Reserve a seat.
def reserve(self):
if self.seats:  # Check if there are available seats in the list.
reserved_seat = heapq.heappop(self.seats)  # Get the smallest seat number from the list.
return reserved_seat  # Return the reserved seat number.
else:
return -1  # Return -1 to indicate that there are no available seats.
​
# Unreserve a seat.
def unreserve(self, seat_number):
if 1 <= seat_number <= self.n:
heapq.heappush(self.seats, seat_number)  # Add the unreserved seat back to the list.
```