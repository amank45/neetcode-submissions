class Solution {
public:
    int maxSubArray(vector<int>& nums) {
         int n = nums.size() ;
         int count = 0;
         int mx = INT_MIN;

         for(int i=0;i<n;i++){
            int temp = nums[i] ;
            count += temp ;
            mx = max(count,mx) ;

            if(count <= 0){
                count = 0;
            }
         }

         return mx  ;
    }
};
