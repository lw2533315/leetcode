// Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

// For example,
// Given the following matrix:

// [
 // [ 1, 2, 3 ],
 // [ 4, 5, 6 ],
 // [ 7, 8, 9 ]
// ]
// You should return [1,2,3,6,9,8,7,4,5].

//按照题目要求遍历matrix，调整row，col值

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>res;
        int max_val = 2222222 ;
        int m = matrix.size();  //行
        if (m == 0)
            return res;
        int n = matrix[0].size(); //列
        if (n == 0)
            return res;





        int row = 0;
        int col = 0;

        while(true){

			//向右
            while (col < n && matrix[row][col] !=max_val){

                res.push_back (matrix[row][col]);

                if (res.size() == m*n)
                    return res;
               matrix[row][col] = max_val;
                col += 1;
            }
            col -= 1;
            row += 1;


             //向下
            while ( row < m  && matrix[row][col] !=max_val ){


                res.push_back (matrix[row][col]);


                if (res.size() == m*n)
                    return res;

                matrix[row][col] =max_val;

                row += 1;


            }

            row -= 1;
            col -= 1;

			//向左
            while (col >= 0   && matrix[row][col] !=max_val  ){
                res.push_back (matrix[row][col]);
                if (res.size() == m*n)
                    return res;
                matrix[row][col] = max_val;
                col -= 1;
            }

            col += 1;
            row -= 1;

			//向上
            while (row >= 0   &&  matrix[row][col] !=max_val  ){
                res.push_back (matrix[row][col]);
                if (res.size() == m*n)
                    return res;
                matrix[row][col] =max_val;
                row -= 1;
            }

            row += 1;
            col += 1;

        }

    }
};