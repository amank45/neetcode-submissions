class DSU:
    def __init__(self,nums):
        self.parent = {n:n for n in nums}
        self.size = {n:1 for n in nums}
        self.maxsize = 1 if nums else 0 
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unionbysize(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx != rooty :
            if self.size[rootx] < self.size[rooty]:
                self.parent[rootx] = rooty 
                self.size[rooty] += self.size[rootx]
                self.maxsize = max(self.maxsize,self.size[rooty]) 
            else:
                self.parent[rooty] = rootx 
                self.size[rootx] += self.size[rooty]
                self.maxsize = max(self.maxsize,self.size[rootx])



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        unique_nums = set(nums) 
        dsu = DSU(unique_nums)

        for n in unique_nums:
            if(n+1) in unique_nums:
                dsu.unionbysize(n,n+1)

        return dsu.maxsize ;

        