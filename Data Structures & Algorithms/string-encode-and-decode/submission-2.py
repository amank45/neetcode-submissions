class Solution:

    def encode(self, strs: List[str]) -> str:
        s = chr(257)
        ans = "" 
        for i in range (0,len(strs)):
            ans += strs[i] + s

        return ans ;

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while (i < len(s)):
            st = ""
            while (s[i] != chr(257)):
                st += s[i] 
                i += 1
                if s[i] == chr(257) :
                    break 
                
            out.append(st)
            i += 1
        
        return out ;



