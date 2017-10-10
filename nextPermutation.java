// Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

// If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

// The replacement must be in-place, do not allocate extra memory.

// Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
// 1,2,3 → 1,3,2
// 3,2,1 → 1,2,3
// 1,1,5 → 1,5,1

// 后来才发现原来是数学中的排列组合，比如“1，2，3”的全排列，依次是：

// 1 2 3
// 1 3 2
// 2 1 3
// 2 3 1
// 3 1 2
// 3 2 1
// 1 2 3
// 所以题目的意思是，从上面的某一行重排到期下一行，如果已经是最后一行了，则重排成第一行。

// 但是也不能根据给出的数组中的数字列出所有排列，因为要求不能占用额外的空间。


class Solution {
    public void nextPermutation(int[] nums) {
        int len = nums.length;
        if (len == 0) return;
        if (len == 1) return;
        
		//一个对比的模板（从小到大排序
		int [] temp = new int[len];
        for (int i = 0; i< len ; i++){
            temp[i] = nums[i];
        }
        Arrays.sort(temp);
		
		//存放处理点开始到最后的所有元素
        List <Integer> pattern = new ArrayList<>();
        pattern.add(nums[len -1]);
        int index = -1;
        for (int i = len-2; i>=0; i--){
            pattern.add(nums[i]);
            //找到一个点比之前的点的元素小，那么就是从这点开始修改
			//12376
			//12 376 就是这个点，从3开始都进入list
            if (nums[i] < nums[i+1]){
				index  = i;   //记录下这点在nums中的下标
                break;
            }
        }
        
       //没有找到这个点那么直接转成从小到大排序
        if (index == -1)
			for(int i = 0; i< len; i++)
                nums[i] = temp[i];
        
		
		else{
			Collections.sort(pattern);
            int temp_int = nums[index];
           
        for(int i = 0; i < pattern.size(); i++){
            if (temp_int < pattern.get(i)){    //找到第一个大于这个点的值得数（在list里）
                nums[index] = pattern.get(i);  //这个数放回nums
                pattern.remove(i);
                break;
            }
        }
			//把这个数以外的所有数都放入数组（sorted以后的）
            for(int i = 1 ; i <= pattern.size(); i++)
                nums[index + i] = pattern.get(i-1);
        }
        
    }
}