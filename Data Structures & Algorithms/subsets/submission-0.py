class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]
        for i in nums:
            
            new_subset = []
            for curr in ans:
                new_subset.append(curr + [i])
            
            ans.extend(new_subset)
            

        
        return ans ;
        