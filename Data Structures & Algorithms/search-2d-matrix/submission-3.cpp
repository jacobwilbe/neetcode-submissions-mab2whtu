class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0, r = matrix.size() - 1;
        int middle_row = 0;

        while (l <= r){
            //middle row in matrix, outside binary search
            middle_row = l + ((r - l) / 2);
            vector<int> list = matrix[middle_row];
            //inner binary search
            int l_val = 0, r_val = list.size() - 1;
            if(target < list[l_val]){
                r = middle_row - 1;
            } else if(target > list[r_val]){
                l = middle_row + 1;
            } else{
                while (l_val <= r_val) {
                    int sub_mid = l_val + ((r_val-l_val) / 2);
                    if (list[sub_mid] == target){
                        return true;
                    } else if(list[sub_mid] < target) {
                        l_val = sub_mid + 1;
                    } else if(list[sub_mid] > target) {
                        r_val = sub_mid - 1;
                    }
                }
                return false;
            }
        }
        return false;
    }
};
