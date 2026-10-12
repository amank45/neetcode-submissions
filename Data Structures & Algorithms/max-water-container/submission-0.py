class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        a = 0
        b = n-1
        ans = 0 
        while a < b:
            vol = min(heights[a], heights[b]) * (b-a) 
            ans = max(ans,vol)

            if(heights[a] < heights[b]):
                a+=1
            else:
                b-=1

        
        return ans ;