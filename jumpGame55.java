// Given an array of non-negative integers, you are initially positioned at the first index of the array.

// Each element in the array represents your maximum jump length at that position.

// Determine if you are able to reach the last index.

// For example:
// A = [2,3,1,1,4], return true.

// A = [3,2,1,0,4], return false.

// 把标记放到倒数第二位看起，往前看，如果所有未的值都小于该位到最后一位的位差，
// 那么不可能跳到最后一位，否则把标记移动到该为上只要从第一位开始有可能跳到该位就能跳到
// 最后一位


class Solution {
    public boolean canJump(int[] nums) {
        int flag_length = nums.length - 1;
        int index = nums.length - 2;
        for (; index >=0; index --){
            if (nums[index] >= flag_length- index)
                flag_length = index;

        }

        if (flag_length == 0)
            return true;
        else
            return false;

    }
}