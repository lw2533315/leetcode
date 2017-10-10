#include<bits/stdc++.h>
using namespace std;

/*Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

1 排序
2 一第一个数为参照，随后的一个数与最后一个数之和与参照做比较，如果小于0，那么前面的数往后前进，增大； 如果大于0，那么后面的数往前进，减小。
3 前面的数和后面的数相遇，本次循环结束*/

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int size = nums.size();
        vector<vector<int> > v;
       
        if (size <=2 )
            return v;
        
         sort(nums.begin(), nums.end());
      
        
        for(int i =0; i< size; i++){
            int val = nums[i];  
			cout<<"the "<<i<< "th value is "<<nums[i]<<endl;
            int j = i+1;
			int k = size - 1;
            while(j < k){
				cout<<"j is "<<j << " and k is "<<k<<endl;
                if (nums[k] + nums[j] + val > 0){
                    k--;
                }else if (nums[k] + nums[j] + val < 0)
                    j++;
                else{
					cout<<"test1~"<<endl;
                    vector<int> v_insert;
                    v_insert.push_back(nums[i]);
                     v_insert.push_back(nums[j]);
                     v_insert.push_back(nums[k]);
                    v.push_back(v_insert);
                    j++;
                    k--;
					
					//避免重复
					//当前面数之后与当前相同那么移动指针
                    while(i<k && nums[j] == nums[j-1]) j++;
					
					//当后面的边界的数与前一个相同，移动指针
                    while(i<k && nums[k] == nums[k-1]) k--;
                }
            }
			
			//下一个参照数与当前相同，移动指针
            while(i< size && nums[i+1] == nums[i]) i++;
        }
		
		cout<<"size of v is "<<v.size()<<endl;
        return v;
        
       
        
     
    }
};
int main() {
	Solution s;
	vector<int> nums;
	nums.push_back(-1);
	nums.push_back(0);
	nums.push_back(1);
	nums.push_back(2);
	nums.push_back(-1);
	nums.push_back(-4);
	cout<<s.threeSum(nums).size();
	return 0;
}