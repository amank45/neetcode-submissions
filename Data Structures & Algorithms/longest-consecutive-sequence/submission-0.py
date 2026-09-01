class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums) 
        num_set = set(nums) 
        maxsize = 0
        for it in num_set:
            if (it-1) not in num_set:
                count = 1
                currit = it
                while (currit+1) in num_set:
                    currit += 1
                    count += 1
                
                maxsize = max(maxsize,count) 

        return maxsize 



        