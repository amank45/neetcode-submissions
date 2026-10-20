class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lm , rm = 0 , 0
        l , r = 0 , n-1 
        vol = 0 
        while l < r:
            if height[l] < height[r]:
                if lm <= height[l]:
                    lm = height[l]
                else:
                    vol += lm - height[l]
                l += 1
            else:
                if rm <= height[r]:
                    rm = height[r]
                else:
                    vol += rm - height[r]
                
                r -= 1

        
        return vol ;
        




        