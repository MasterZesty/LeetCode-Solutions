class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

#         # RecursionError : max recursion depth
#         def next_possible_t(time,trips,totalTrips,counter):
            
#             #print(time,trips,counter)
            
#             if sum(trips) >= totalTrips:
#                 return counter
            
#             counter += 1
#             for i,val in enumerate(time):
#                 #print(counter,' for loop : ',val,(time[i]%counter==0))
#                 if (time[i] == 1):
#                     trips[i] += 1
#                 elif time[i]%counter==0 and counter !=1:
#                     trips[i] += 1
                    
            
            
#             return next_possible_t(time,trips,totalTrips,counter)
        
        
#         t = (next_possible_t(time,[0]*len(time),totalTrips,0))
        
#         return t

          #Approch 2 : can be solved using binary serarch
        def time_possible(mid,time,totalTrips):
            trips= 0
            for i,val in enumerate(time):
                trips+= mid//time[i]
            
            return (trips>= totalTrips)
                
        start = 1
        end = 100000000000000 # 1e14
        
        while start < end:
            
            mid = (start+end)//2
            
            if (time_possible(mid,time,totalTrips)):
                end = mid
            else:
                start = mid + 1
                
        return start
        