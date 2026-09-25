class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> thelist;
        for (int n : nums){
            
            if (thelist.count(n)){
                return true;
            }
            thelist.insert(n);

        }
        return false;
    }
};