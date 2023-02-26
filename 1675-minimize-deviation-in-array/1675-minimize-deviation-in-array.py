class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # ref video : https://youtu.be/WTEbQxZq_Ew
        # first make all odd element even so that => 
        # even element can be incresed => rule divide by 2
        
        # from queue import PriorityQueue
        
        # pq = PriorityQueue()
        
        
        # max_e = max(nums)
        # min_e = min(nums)
        # print(nums)
        # for i,val in enumerate(nums):
            # if val%2 != 0:
                # nums[i] = val*2
                
            # pq.put(nums[i])
        # print(nums)
        
        # now we will reduce our even nums such that =>
        # reduce current max by divide by 2 => update current max => 
        # reduce current max divide by 2
        # till current max becomes odd and rule odd nums can be decresed 
        
        # from queue import PriorityQueue
        # pq = PriorityQueue()
        
        # min_dev = max_e - min_e
        
        
        # we will loop until max element becomes odd
        # while not pq.empty():
            # top = pq.get()
            # if top % 2 == 0:
                # min_dev = min(min_dev, top - min_e)
                # print(min_dev)
                # top //= 2
                # min_e = min(min_e, top)

                # pq.put(top)
                
            # else:
                # break
        
        # get that odd element 
        # top = top
        # min_dev = min(min_dev, top - min_e)
        
        # return min_dev
            
        import heapq

        n = len(nums)
        maxe = float('-inf') # equivalent to INT_MIN in C++
        mine = float('inf') # equivalent to INT_MAX in C++
        pq = []

        for i in range(n):
            if nums[i] % 2 != 0:
                nums[i] *= 2
            maxe = max(maxe, nums[i])
            mine = min(mine, nums[i])
            heapq.heappush(pq, -nums[i]) # using heapq to simulate a max-heap

        ans = maxe - mine

        while -pq[0] % 2 == 0:
            top = -heapq.heappop(pq)

            ans = min(ans, top - mine)
            top //= 2
            mine = min(mine, top)
            heapq.heappush(pq, -top)

        ans = min(ans, -pq[0] - mine)
        return ans

        
        
        
        