# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# 递归法超时，只是用来测验和查找规律

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        l = [0]
        self.move(1,1,m,n,l)
        return l[0]
    def move(self, row,col,m,n,l):
        if row == m and col == n:
            l[0] += 1
        elif row > m or col > n:
            pass
        else:
            self.move(row + 1, col,m,n,l)
            self.move(row, col + 1, m,n, l)

        
s = Solution()
print (s.uniquePaths(3,2))
