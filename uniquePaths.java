// A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

// The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

// How many possible unique paths are there?

// 之前用recursive写了一个在同名文件_test.py，发现会超时，只能回头找规律
// 发现 m = 2 时 n是多少 就有多少种方法  （2,5）方法5   （2,4）方法4， （2,1） 方法1
// 当m = 3时，通过左上角点（1,1） 可以一共获得（2，n)+(2,n-1),+ ...+(2,1) 种方法
// 左数第二个点 （1,2) 开始到 finish点时一个 （3,n-1)矩阵，一共有 （2，n-1)+ (2,n-2)+...+(2,1)种方法

// 从m=2开始把 方法数都存在一个arraylist里，然后每加一层更新arraylist，每个item（ways）代表着从
//这个点出发的方法数，方法数 = 右侧一格的方法数 + 下面一格的方法数

class Solution {
      public int uniquePaths(int m, int n) {
         
        if (m == 1 || n == 1)
            return 1;
        
        if (m == 2)
            return n;
        List<Integer> ways = new ArrayList<>();
        while (n>0){
            ways.add(n --);
                
        }
          
        int leve = 3;
        while (leve <= m){
            List<Integer> temp = new ArrayList<>(ways);
            int index = temp.size() -1;
            int rightValue = 0;
            for( ; index >=0; index -- ){
                rightValue += temp.get(index);
                ways.set(index,rightValue);
            }
            
            leve ++;
        }
        
        return ways.get(0);
    }
}