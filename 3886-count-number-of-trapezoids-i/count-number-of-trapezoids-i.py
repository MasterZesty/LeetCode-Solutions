class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        '''
        For a line parallel to the x‑axis, all its points must share the same y‑coordinate.
        Group the points by their y‑coordinate.
        Choose two distinct groups (two horizontal lines), and from each group select two points to form a trapezoid.


        The nCr combination formula is nCr = n! / (r! * (n-r)!), where 'n' is the total number of items and 'r' 
        is the number of items to choose. This formula calculates the number of ways to choose 'r' items 
        from a set of 'n' items without regard to the order of selection. 
        '''
        c = {}
        ans = 0
        mod = 10**9 + 7

        # how many points lie on each horizontal line (grouped by y-coordinate).
        for p in points:
            x = p[0]
            y = p[1]

            if c.get(y, -1) == -1:
                c[y] = 1
            else:
                c[y] += 1

        # number of pairs on each horizontal line
        t = []
        total_num_of_pairs = 0
        for y, no_of_points in c.items():
            n = no_of_points
            r = 2
            # num_of_pairs = n! / 2 * (num_of_pairs - 2)!
            num_of_pairs = int( n * (n-1) / 2 )

            total_num_of_pairs += num_of_pairs

            t.append([y, num_of_pairs])

        

        # print(t)

        # if no horizontal pairs, no trapezoid
        if total_num_of_pairs == 0:
            return 0

        
        ans = 0
        # computes all possible combinations of pairs from different horizontal lines
        # double counting - pair from line A and pair from line B
        # and again pair from line B and pair from line A
        # so ans//2
        for j, i in t:
            # print(j,i)
            ans += (total_num_of_pairs - i) * i % mod

        return (ans//2 )%mod

