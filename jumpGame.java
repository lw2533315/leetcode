// Given an array of non-negative integers, you are initially positioned at the first index of the array.

// Each element in the array represents your maximum jump length at that position.

// Your goal is to reach the last index in the minimum number of jumps.

// For example:
// Given array A = [2,3,1,1,4]

// The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

// Note:
// You can assume that you can always reach the last index.

class Solution {
    public int jump(int[] nums) {
        int index = 0;
        int last_index = nums.length-1;
        int steps = 1;
        if(nums.length == 1 )
            return 0;
        if (nums[0] == 0)
            return -1;
        while(index < last_index){
            if (nums[index] + index >= last_index)
                return steps;
            if (nums[index] == 1){
                steps++;
                index++;
            }else {

					//(1,4,3,2,1,5,6)  当index = 1时， 因为值是4，所以index =2,3,4,5，都可以通过一次
					//jump 到达，但是我们要看这4个index+index对应的值最远能到哪，我们取最远的那个
                    int target = index+1+nums[index+1];
                        int gap = 1;
                    for(int i =2 ;i<=nums[index]; i++){
			            if (index+i + nums[index+i] > target){
                            target = index+i +nums[index+i];
                            gap = i;
                        }


                    }
                    index+=gap;
                    steps++;
            }

        }
        return steps;
    }
}