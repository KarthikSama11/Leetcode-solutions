class Solution {
public:
    void dfs(int i, vector<int> &arr, vector<int> &nums, vector<vector<int>> &ans){
      if(i >= nums.size()){
        ans.push_back(arr);
        return;
      }
      
      dfs(i + 1, arr, nums, ans);
      arr.push_back(nums[i]);
      dfs(i + 1, arr, nums, ans);
      arr.pop_back();
      return;
    }
    vector<vector<int>> subsets(vector<int>& nums) {
      vector<vector<int>> ans;
      vector<int> arr;
      dfs(0,arr, nums, ans);
      return ans;
    }
};