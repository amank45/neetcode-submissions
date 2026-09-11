class Solution:
    def recur(self,nums:List[int],ans:List[List[int]],target:int,temp:List[int],idx:int) -> none:
        if target == 0:
            ans.append(temp.copy())
            return 
        n = len(nums)

        for i in range(idx,n):
            if nums[i] > target:
                continue 

            temp.append(nums[i])
            self.recur(nums,ans,target-nums[i],temp,i)
            temp.pop()

        return 
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

       ans = []
       temp = []

       self.recur(nums,ans,target,temp,0) 

       return ans ; 

        