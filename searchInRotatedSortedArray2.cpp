//不能用中间跟target比较，那样情况太多，需要判断中间点时在递增的哪个部分
//应该用nums[m] 跟nums[l]比较或者 num[m]比较
//这两个才是关键点

class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0;        
        int r = nums.size() - 1;
        if (r == -1)
            return false;
        
     
        while (l <= r){
            int m = (l + r) / 2;
            if (nums[m] ==  target)
                return true;
            if (nums[m] > nums[l]){ //l - m 是有序的
                if (nums[l] == target)
                    return true;
                else if (target > nums[l] && target < nums[m]){
                    r = m - 1;
                    
                }else
                    l = m + 1;
                
            }
            else if(nums[m] < nums[l]){ //m - r是有序的
                if (nums[r] == target)
                    return false;
                else if (target < nums[r] && target > nums[m]){
                    l = m + 1;
                }
                else
                    r =  m - 1;
            }
            else
                l++; 
        }
        return false;
           
          
    }
};