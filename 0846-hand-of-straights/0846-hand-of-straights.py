class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        we have n number of cards in hand hand[i] is tyhe value on ith card
        - divide cards into groups of size k
        - and that group consist of a k consecutive cards
        
        hand = [1,2,3,6,2,3,4,7,8] k = 3
        
        [1,2,3] [2,3,4] [5,6,8]
        
        approch - https://leetcode.com/problems/hand-of-straights/discuss/135655/Python-O(nlgn)-simple-solution-with-intuition
        
        O(nlgn) 

        Given test case like hand = [1,1,1,2,2,2,3,3,3], W = 3, what do you think?

        My thought is: If I know the first number in one of the group, I know the whole group.

        e.g. If i know the first number in a group is 1 and W == 3, then the group must be [1, 2, 3].

        That is to say, I just need to find all starting numbers of each group, then go check if all the other numbers in the group can be found in the given hand.

        First suppose we know the starting number of each group. The question is: How do you know if the other numbers of the group exist in hand?

        Like if we know 2 must be the starting number in a group of length 3, then we immediately know that the group consists of [2,3,4].

        To check if 3 and 4 exist in hand, we can just use a hash table to find this out.

        Still, there might be groups with the same starting number, like if group_1 and group_2 both have starting number 2, how do you know if there are two 3s and 4s?

        This can be easily solved by storing each number's time of appearence in the hash table, like a Python dictionary or a C++ std::unordered_map.

        Each time we used a number, we decrease its counts, once its counts is 0, we know the number is no longer available.

        Final question is: How do you find the starting number of each group?
        We can get some intuition by observing an example:

        hand = [1, 2, 3, 3, 4, 5] and W = 3
        We know that there are 2 groups and their corresponding starting numbers are 1 and 3. How do we find this out?

        We can easily find the starting number of the first group, namely 1. It's just the minimum of the given hand. Then we automatically constructed the group [1,2,3]. After that, the minimum of remaining numbers in hand is 3, of course it's the starting number of the other group!

        Yes, we can iteratively find the minimum after each group's construction. To achieve this, we can use a minimum heap. Each time we want to find a starting number, we pop the heap. If the number is no longer available, we pop again until we find the minimum of the remaining numbers.
         
        
        """
        
        n = len(hand)
        k = groupSize
        hm = {}
        
        if k == 1:
            return True
        
        if n%k != 0:
            return False
        
        for i,v in enumerate(hand):
            hm[v] = hm.get(v,0) + 1
            
        # print(f"hm:{hm}")
        
        from heapq import heappop, heapify
        
        heapify(hand)
        for i in range(n//k):
            start = heappop(hand)
            while hm[start] == 0:
                start = heappop(hand)
            
            for _ in range(k):
                hm[start] = hm.get(start,0) - 1
                if hm[start] < 0:
                    return False
                
                start += 1
            
        
        return True