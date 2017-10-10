// Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

// For example,
// Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


//反复找最高点
class Solution {
    public int trap(int[] height) {

        int [] sum = new int [] {0};

		//一开始去掉两头的0，高度0对蓄水毫无帮助
        int left = 0;
        for (int i = 0; i<height.length; i++) {
            if (height[i] == 0)
                left ++;
            else
                break;
        }

         int  right = height.length - 1;
        for (int i = height.length -1; i>=0 ; i--){
            if (height[i] == 0 )
                right -= 1;
            else
                break;
        }


		//长度小于2 是不可能形成 凹陷蓄水的，最少为3
        if (height.length <= 2)
            return 0;


        recur(left,right,sum,height);

        return sum[0];


    }

    public void recur(int left, int right, int [] sum, int[] height){

        //调用时进来的left，和right 下标相连，不可能蓄水
        if (left+1 >= right) return;
        int max = height[left + 1];
        int index = left + 1;

		//找到除left 和right外最高点
        for (int i = left +1; i < right; i++){
            if (max<height[i]){
                max = height[i];
                index = i;
            }
        }

		//当最高点小于left和right对应的高度，证明整个这一段都是低洼地可以蓄水
        int temp = Math.min(height[left], height[right]);
        if (max <= temp){
            for (int i = left+1; i < right; i++) {
				//以两头低点为标准减去高度
                sum[0] += temp - height[i] ;
            }

        }

		//如果两头之间还有 高点继续recursive
        else {
        recur(left, index, sum, height);
        recur(index,right, sum, height);
        }
    }
}