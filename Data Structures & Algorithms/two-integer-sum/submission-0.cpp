class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size() ;
        unordered_map<int,int> comp(n) ;
        int a = -1 , b = -1 ;
        for(int i=0;i<n;i++){
            int c = target - nums[i] ;
            if(comp.find(c) != comp.end()){ a = i ; b = comp[c] ; break ;}
            else{
                comp[nums[i]]=i ;
            } 
        }

        vector<int> ans ;
        if(a<=b){
            ans.push_back(a);
            ans.push_back(b);
        }
        else{
            ans.push_back(b);
            ans.push_back(a);
        }

        return ans ;
    }
};
