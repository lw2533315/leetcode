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
        List <Integer> list = new ArrayList<>();
        int times = 1;
        if(nums.length == 1 )
            return 0;
        if (nums[0] == 0)
            return -1;
        recur(0, nums, times,list);
        int jumps = nums.length;
        for(int i = 0 ; i< list.size(); i++){
            if (list.get(i)< jumps)
                jumps = list.get(i);
        }
        return jumps;

    }
    public void recur(int begin, int[]nums, int times, List<Integer> list){
        if(begin >= nums.length)
            return;
        if (nums[begin] == 0)
            return;
        if (begin + nums[begin] >=nums.length -1){
            list.add(times);

            return;
        }
        for(int i =1 ;i<=nums[begin]; i++){
            recur(begin+i, nums, times+1, list);
        }

    }
}