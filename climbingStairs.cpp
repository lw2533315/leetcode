
// You are climbing a stair case. It takes n steps to reach to the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Note: Given n will be a positive integer.

// 从i阶楼梯往上有走i-1 阶的方法加i-2阶的方法



class Solution {
public:
    int climbStairs(int n) {
        vector<int>  v;
        for ( int i = 0; i < n; i++){
            v.push_back(0);
        }
       
        
        if (n == 1 )
            return 1;
        if (n == 2)
            return 2;
        v[n-1] = 1;  //最后step登上去有1种方法
        v[n-2] = 2;  //倒数第二step登顶有2种方法
     
        for(int i = n-3; i>= 0; i--)
        {
            v[i] = v[i+1] + v[i+2];
        }
     
        
        return v[0];
    }
};