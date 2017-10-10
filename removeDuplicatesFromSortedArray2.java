// Follow up for "Remove Duplicates":
// What if duplicates are allowed at most twice?

// For example,
// Given sorted array nums = [1,1,1,2,2,3],

// Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
题目要求是当重复到达3，忽略掉它，并且在原数组中删除，最后行成的新数组前 n位符合
该函数的返回值n。
设置一个指针copy_index 同步于遍历指针i，用于复制i指向的元素到copy_index 的位置，目的是修改原数组，只有当重复到第三次时该指针才回退一位

public class Solution {
	public int removeDuplicates(int[] nums) {
		if (nums.length <= 2){
            return 2;
        }
        
        boolean jump = false;
        int copy_index = 1;
        int t = nums[0];
        int counter = 0;  //记录被删除（覆盖掉的item数）
        for (int i = 1; i < nums.length; i++){
            nums[copy_index++] = nums[i]; //遍历到每一个item都会执行copy
            if (nums[i] == t){
                
                if (jump){
                    counter ++;
                    copy_index --;  //当连续出现duplicate第3次，指针减少1
					//因为该指针在一开始就自加，所以该指针实际在这次循环没有移动
					//因为这个位置是需要被替换的元素。没出现一次duplicate 3次，
					//这个指针就会落后于i指针1个位置
                    
                }else{
                    jump = true;
                    
                }
            }
            else {
                
                t = nums[i];
                jump = false;
            }
        }
        return nums.length - counter;
	}
}