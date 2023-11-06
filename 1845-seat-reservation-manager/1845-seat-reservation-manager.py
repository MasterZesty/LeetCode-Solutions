class SeatManager:

    def __init__(self, n: int):
        
        self.n = n
        self.seats = []
        
        # heapq.heappush(heap, item)
        for i in range(1,n+1):
            heapq.heappush(self.seats, i)

    def reserve(self) -> int:
        # pop the seats make it reserve
        if self.seats:
            reserved_seat = heapq.heappop(self.seats)
            return reserved_seat
        else:
            return -1

    def unreserve(self, seatNumber: int) -> None:
        if 1 <= seatNumber <= self.n:
            heapq.heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)