# Follow up for "Unique Paths":

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.

# [
  # [0,0,0],
  # [0,1,0],
  # [0,0,0]
# ]
# The total number of unique paths is 2.
# 做法类似于 uniquePaths.java  就是在矩阵里多了一个1表示有障碍，对应障碍点的
# 可能的通过方法要设置为 0， 然后区别于uniquePaths 不是从第二层开始作为起始点
# 因为第一层可能出现 障碍物，实际上uniquePaths也应该是把第一层作为参照物


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        
        
        row = len(obstacleGrid);
        if row == 0:
            return 0;
        
        col = len(obstacleGrid[0]);
        if col == 0:
            return 0;
        
        #终点是障碍，返回0   
        if obstacleGrid[row-1][col-1] == 1:
            return 0
        
        ways = [0] * col   #初始化一个有col个0的list
        
		#构建第一层对应的list， 反应每个矩阵的格子可能对应的通过方法
        find_1 = False
        index = col -1
        while index >= 0:
            if obstacleGrid[row -1][index] == 0 and find_1 == False:
                ways[index] = 1
            elif obstacleGrid[row-1][index] == 1:  #一旦出现第一个障碍物，那么
													#在障碍物左侧的所以格子都应该设为0
                ways[index] = 0;
                find_1 = True
            else:
                ways[index] = 0
            index -= 1
                
           
        
		#这里对比uniquePath 也有改动，应为可能在任何一层都出现障碍物，为了
		#方便查看对应的格子是否是障碍物，设置level于对应的行数index对应
		#第一层已经拿出来单独讨论了，所以这里从倒数第二层开始计算
        level = row - 2; #当前的row_index
     
        while level >= 0:
            
            temp = ways[:];   #深度复制，不会指向同一个引用
            temp_last_index = len(temp) - 1;
            new_value = 0;   #保留右侧的格子对应的走出去的可能性
            while temp_last_index >= 0:
                if obstacleGrid[level][temp_last_index] == 0:
                    new_value += temp[temp_last_index];
                    
                else:
                    new_value = 0    #因为该点时障碍所以，以该点为右侧的道路数为0
                    
                ways[temp_last_index] = new_value;
                temp_last_index -= 1;
              
                    
            level -= 1
        
        return ways[0];
            
        