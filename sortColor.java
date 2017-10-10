
// Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

// Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

// Note:
// You are not suppose to use the library's sort function for this problem.

// 遍历数组nums，用三个临时变量记录下0,1,2的个数，然后对nums数组重新赋值
class Solution {
    public void sortColors(int[] nums) {
        int nums_len = nums.length;
        int temp0 = 0;
        int temp1 = 0;
        int temp2 = 0;
        for (int i = 0; i<nums_len; i++){
            if (nums[i] == 0){
                temp0 += 1;
            }
            if (nums[i] == 1){
                temp1 += 1;
            }
            if (nums[i] == 2){
                temp2 += 1;
            }
        }
        for (int i = 0; i<temp0; i++)
            nums[i] = 0;
        for (int i = temp0; i < temp1 +temp0; i++)
            nums[i] = 1;
        for (int i = temp1 +temp0; i < temp1 +temp2 + temp0; i++)
            nums[i] = 2;
        
    }
}