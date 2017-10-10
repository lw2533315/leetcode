// Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

// Each number in C may only be used once in the combination.

// Note:
// All numbers (including target) will be positive integers.
// The solution set must not contain duplicate combinations.
// For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
// A solution set is:
// [
  // [1, 7],
  // [1, 2, 5],
  // [2, 6],
  // [1, 1, 6]
// ]
class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> list = new ArrayList<>();

        recur(list, new ArrayList<>(), candidates, target, 0);
        return list;

    }

    public void recur (List<List<Integer>> l, List<Integer> temp, int []candidates, int sub, int begin ){
        if (sub < 0) return;
        else if (sub == 0) l.add(new ArrayList<>(temp));
        else {
            for (int i = begin; i< candidates.length; i++){
                    if (i>begin && candidates[i] == candidates[i-1]) continue; //防止重复的出现
					//如[1,1,2,5,7] target 8   index = 0 call recur() “1” 放入了temp 可以在（1,2,5,7）选
					// 1+2+5 = 8； index = 1 call recur（）  “1” 放入temp 可以在（2,5,7）里选 1+2+5 = 8
					//出现重复
                    temp.add(candidates[i]);
                    recur(l,temp, candidates,sub - candidates[i] , i+1);
                    temp.remove(temp.size() -1);
                }
            }
        }
    }