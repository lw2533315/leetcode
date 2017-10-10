// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.


//用vector一行一行表示从每个格子对应的最短的路径的距离

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = grid.size();
        if (row == 0)
            return 0;
        int col = grid[0].size();
        if (col == 0)
            return 0;
        
        //把最底下一层的距离存放在对应vector里
        vector<int> path;
        
        for(int i = 0; i < col; i++)
            path.push_back (0);
        
		//从最后一行的最右开始计算距离，每个格子到终点的距离是自己的值+ 右侧的值
        int right_val = 0;    //终点右侧的值是0
        for(int i = col - 1; i >=0; i--){
            path[i] = right_val + grid[row - 1][i];
            right_val = path[i];
        }
            
        int level = row - 2;
        
        while (level >= 0){
            vector<int> temp(path);
            right_val = 0x7fffffff;   //除了最后一行每行最后一个col的格子不可能往右走
            for(int i = temp.size() -1; i>=0; i--){//从最后面开始计算
                if (temp[i] > right_val)  //往下比较近
                    path[i] = grid[level][i] + right_val;
                else
                    path[i] = grid[level][i] + temp[i];
                right_val = path[i];    //更新右侧的距离
            }
            level --;
            
        }
        return path[0];
        
    }
};