class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& s) {
        unordered_map<string, vector<string>> m;
        for (auto &w : s) {
            string k(26, 0);
            for (char c : w) k[c - 'a']++;
            m[k].push_back(w);
        }
        vector<vector<string>> r;
        for (auto &p : m) r.push_back(p.second);
        return r;
    }
};
