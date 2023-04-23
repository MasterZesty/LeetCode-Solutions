#User function Template for python3

def isSubset( a1, a2, n, m):
    
    a1_hmap = {}
    a2_hmap = {}
    flag = True
    
    for e in a1:
        if e not in a1_hmap.keys():
            a1_hmap[e] = 1
        else:
            a1_hmap[e] += 1
            
    for e in a2:
        if e not in a2_hmap.keys():
            a2_hmap[e] = 1
        else:
            a2_hmap[e] += 1
    
    # print(a1_hmap,a2_hmap)
    
    for key,value in a2_hmap.items():
        try:
            if a1_hmap[key] >= value:
                # print('iteam exist in both dict')
                flag = True
            else:
                # print('item exist in both but not macth value')
                flag = False
                break
        except:
            # print('exception')
            # print('new item key error')
            flag = False
            break
            
    
    if flag:
        return "Yes"
        
    return "No"



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends