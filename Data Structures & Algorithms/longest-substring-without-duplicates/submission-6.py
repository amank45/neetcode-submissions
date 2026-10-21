class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if s == 0 :
            return 0

        if s == 1:
            return 1 

        l = 0
        size = 0
        mp = {}

        for i in range(0,n):
            tempsize = 0
            c = s[i]

            if c not in mp or mp[c]<l:
                mp[c] = i
                tempsize = i - l + 1
            else:
                l = mp[c] + 1
                mp[c] = i
                tempsize = i - l + 1

            size = max(size,tempsize)

        return size ; 



                
            
        
        