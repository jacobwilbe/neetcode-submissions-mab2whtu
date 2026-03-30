class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        //every time we swap a non val value, we 
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};