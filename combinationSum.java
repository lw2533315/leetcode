// Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

// The same repeated number may be chosen from C unlimited number of times.

// Note:
// All numbers (including target) will be positive integers.
// The solution set must not contain duplicate combinations.
// For example, given candidate set [2, 3, 6, 7] and target 7,
// A solution set is:
// [
  // [7],
  // [2, 2, 3]
// ]


class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> list = new ArrayList<>();
        recur(list, new ArrayList<>(), candidates, target, 0);
        return list;
    }

    public void recur(List<List<Integer>> l, List<Integer> temp, int[] nums, int remainder, int begin){
        if (remainder < 0) return;
        else if (remainder == 0) l.add(new ArrayList<>(temp));  //复制构造函数
        else {
            for (int i = begin ; i< nums.length; i++){

				//temp 改变后必须改回来
                temp.add(nums[i]);
                recur(l, temp, nums, remainder - nums[i], i );
                temp.remove(temp.size() -1);
            }
        }


    }
}