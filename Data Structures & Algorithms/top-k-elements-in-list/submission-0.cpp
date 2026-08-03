class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> mp;
        for (int &t : nums) {
            mp[t]++;
        }
        
        // Index represents frequency, value is list of numbers with that frequency
        vector<vector<int>> buckets(nums.size() + 1);
        for (auto &[num, count] : mp) {
            buckets[count].push_back(num);
        }
        
        vector<int> ans;
        // Iterate backwards from highest possible frequency
        for (int i = buckets.size() - 1; i >= 0 && ans.size() < k; --i) {
            for (int num : buckets[i]) {
                ans.push_back(num);
                if (ans.size() == k) break;
            }
        }
        return ans;
    }
};
