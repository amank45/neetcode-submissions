class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers) 
        my_map = dict() 


        for i in range(n):
            c = target- numbers[i] 
            if c in my_map:
                return [my_map[c]+1,i+1]
            
            if c not in my_map:
                my_map[numbers[i]] = i 
        

        return [0,0] ;