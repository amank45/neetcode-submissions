class Solution:
    def recur(self,nums:List[int],ans:List[List[int]],target:int,temp:List[int],idx:int) -> none:
        if target == 0:
            ans.append(temp.copy())
            return 
        n = len(nums)
        if target < 0 or idx >= n:
            return

        temp.append(nums[idx])
        self.recur(nums,ans,target-nums[idx],temp,idx)
        temp.pop()
        
        self.recur(nums,ans,target,temp,idx+1) 
        return 
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

       ans = []
       temp = []

       self.recur(nums,ans,target,temp,0) 

       return ans ; 

        