class Solution:
    def threeSum(self, temp: List[int]) -> List[List[int]]:
        n = len(temp)
        
        nums = sorted(temp) 
       # if temp[n-1] < 0 or temp[0] > 0:
        #    return []
        ans = set()
        for i in range(0,n):
            a = -nums[i]

            j = i+1
            k = n-1
            while j < k:
                if nums[j] + nums[k] == a:
                    t = tuple(sorted([nums[i], nums[j], nums[k]]))
                    ans.add(t)
                    j += 1
                    k -= 1
                     
                elif nums[j] + nums[k] < a:
                    j += 1
                else:
                    k -= 1

        return [list(m) for m in ans]
                


        




