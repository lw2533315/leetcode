// Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

// For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
// the contiguous subarray [4,-1,2,1] has the largest sum = 6.
// 通过找子串的结束点来找答案
// max_ending，记录到当前点的子串的最大和
// 检测每个点时如果发现 max_ending < 0 就要从新开始记录  -2,1,-3,4
// 一开始max_ending = -2,当i = 1时，抛弃，因为从i = 0 开始到i = 1一定
// 比直接i = 1时的值小，同理当i= 3时，nums[2] = -3, max_ending<0,
// 所以max_ending = -2被抛弃，max_ending  = 4
// 每当发现max_ending 比记录最大值得max_so_far大时，修改他

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;

        int max_ending = nums[0];
        int max_so_far = nums[0];

        for(int i = 1; i < nums.size(); i++){
            if (max_ending < 0)
                max_ending = nums[i];
            else
                max_ending += nums[i];

            max_so_far = max(max_so_far, max_ending);
        }

        return max_so_far;
    }

};