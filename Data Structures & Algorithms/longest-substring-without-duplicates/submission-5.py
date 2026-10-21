class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if s == 0 :
            return 0

        if s == 1:
            return 1 

        r , l = 0,0
        size = 0
        mp = {}

        for i in range(0,n):
            tempsize = 0
            c = s[i]

            if c not in mp or mp[c]<l:
                mp[c] = i
                r += 1
                tempsize = r - l
            else:
                l = mp[c] + 1
                mp[c] = i
                r = i+1
                tempsize = r - l

            size = max(size,tempsize)

        return size ; 



                
            
        
        