// Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

// For example,
// Given n = 3,

// You should return the following matrix:
// [
 // [ 1, 2, 3 ],
 // [ 8, 9, 4 ],
 // [ 7, 6, 5 ]
// ]

class Solution {
    public int[][] generateMatrix(int n) {
            //初始化二维数组为0
            int arry  [][] = new int [n][n];
            
        
            int steps = n*n;
            int num = 1;
            int row = 0;
            int col = 0;
			
			//沿着他的规律走一圈，把数字都填上
            while (num <= steps){
                while (col < n && arry[row][col] == 0 ){
                    arry[row][col] = num ++;
                    col += 1;
                    
                }
                col -= 1;
                row += 1;
                
                while (row < n && arry[row][col] == 0){
                    arry[row][col] = num ++;
                    row += 1;
                }
                
                row -= 1;
                col -= 1;
                
                while (col >= 0 && arry[row][col] == 0){
                    arry[row][col] = num ++;
                    col -= 1;
                }
                
                col += 1;
                row -= 1;
                
                while (row >= 0 && arry[row][col] == 0){
                    arry[row][col] = num ++;
                    row -= 1;
                }
                
                row += 1;
                col += 1;
            }
        return arry;
        
        
        
        
        
    }
}