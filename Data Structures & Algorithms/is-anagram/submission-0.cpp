class Solution {
public:
    bool isAnagram(string s, string t) {
       int n = s.size();
       int m = t.size() ;
       if(n!=m) return false ;
       vector<int> freq(27,0) ;

       for(int i= 0;i<n;i++){
          int v1 = s[i] - 'a' ;
          freq[v1]++ ;
          int v2 = t[i]- 'a' ;
          freq[v2]--; 
       }

       for(int i=0;i<27;i++){
        if(freq[i] != 0) return false ;
       }

       return true ; 
    }
};
