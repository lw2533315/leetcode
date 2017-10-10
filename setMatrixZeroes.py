# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row = set();
        col = set();
        for i in range (len(matrix)):
            for j in range (len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
                
        for i in row:
            print ("row item is ", i)
            matrix[i] = [0]*len(matrix[0])
        
        for i in col:
            for j in range (len(matrix)):
                matrix[j][i] = 0
            