# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Given input matrix =
# [
  # [1,2,3],
  # [4,5,6],
  # [7,8,9]
# ],

# rotate the input matrix in-place such that it becomes:
# [
  # [7,4,1],
  # [8,5,2],
  # [9,6,3]
# ]


//可以通过两步实现 1. 从00开始的对角线对调，  2 中垂直线对调
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        //对角线
        i = 0
        size = len(matrix)
        while(i < size):
            j = i+1
            while(j < size):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
                j += 1

            i += 1


        //中垂直线
        i = 0

        half_size = size / 2
        while(i < size):
            j = 0
            while(j < half_size):

                matrix[i][j],matrix[i][size - j -1] = matrix[i][size - j - 1],matrix[i][j]
                j += 1
            i += 1