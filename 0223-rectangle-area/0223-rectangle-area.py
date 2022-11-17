class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # lets do some stuff
        
        area_a= (ax2-ax1)*(ay2-ay1)
        
        area_b = (bx2-bx1)*(by2-by1)
        
        # better understand math behind algo : https://youtu.be/ICtwTFkvFHY
        
        w = (min(ax2,bx2)-max(ax1,bx1))
        b = (min(ay2,by2)-max(ay1,by1))
        
        aoi = 0
        
        if w > 0 and b > 0 :
            aoi = w*b
            
        return(area_a+area_b-aoi)
        
        
        
        
        