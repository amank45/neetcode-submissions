class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size() ;
        unordered_map<int ,bool> freq ;

        int i = 0 , j= n-1 ;
        while(i<j){
            if(freq[nums[i]] == true) return true ;
            else{ freq[nums[i]] = true ; i++ ;}
            if(freq[nums[j]] == true) return true ;
            else{ freq[nums[j]] = true ; j-- ;}
        }

        return false ;
    }
};