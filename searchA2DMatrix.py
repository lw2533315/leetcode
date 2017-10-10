
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.



class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        last_line = True
        row = 0
		
		#两种特殊情况
        if len(matrix) == 0:
            return False;
        if len(matrix[0]) == 0:
            return False
        
        while row < len(matrix):
			#与每行第一个item比较
            if matrix[row][0] < target:   
                row += 1
            elif matrix[row][0] == target:
                return True
			#小于第一行第一个item
            elif matrix[row][0] > target and row == 0:
                return False
            else:
                break
        
        for v in matrix[row -1]:
            if v == target:
                return True
        
        return False
                
        
        
        
        