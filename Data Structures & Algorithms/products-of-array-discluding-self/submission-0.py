class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [] 
        ans = []
         
        premul = 1 
       # pre.append(1)

        for i in range(n):
            pre.append(premul)
            premul *= nums[i] 

        sufmul = 1 
        for i in range(n-1,-1,-1):
            temp = sufmul * pre[i]
            ans.append(temp)
            sufmul *= nums[i]

        l = 0 
        r = n-1 
        while(l<r):
            ans[l],ans[r] = ans[r],ans[l]
            l +=1 
            r -= 1

        return ans ;


        