# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

# For example,
# There exist two distinct solutions to the 4-queens puzzle:

# [
 # [".Q..",  // Solution 1
  # "...Q",
  # "Q...",
  # "..Q."],

 # ["..Q.",  // Solution 2
  # "Q...",
  # "...Q",
  # ".Q.."]
# ]
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        if n == 1:
            return [['Q']]
        
        res = []
        board = []
        for i in range(n):
            board.append([])
        i = 0;
        while i < n:
            j = 0
            while j < n:
                board[i].append('.')
                j += 1
            i += 1
      
            
        self.recur(0,board, n,res) 
        
        
     
        return res
	#递归检测试探道了最后一行以后，证明满足条件
    def recur(self, row,  board,n ,res):
        if row == n:
            temp_res = []
            index = 0
            while index < len(board):
                temp = "".join(board[index])
                temp_res.append(temp)
                index += 1
            res.append(temp_res)
            
        else:
            col = 0
            while col < n:
				#每行发现合适的如果不是最后一列，继续试探
                if self.is_valid(row,col,board,n):
					#合适的列递归调用下一行
                    self.recur(row+1,board,n,res)
                    board[row][col] = '.'
                col += 1
                    
        
            
        
                        
                        
            
        
            
            
    #横竖斜检测       
    def is_valid(self,row, col, board , n):
        board[row][col] = '.'
        if 'Q' in board[row]:
            
            return False
        i = 0
        while i < n:
            if board[i][col] == 'Q':
                
                return False
            i += 1
        
        i = row
        j = col
        
        while i - 1 >=0 and j - 1 >=0:
            if board[i-1][j-1] == 'Q':
                return False;
            i = i-1
            j = j-1
            
        i = row
        j = col
        
        while i + 1 < n and j + 1 < n:
            if board[i+1][j+1] == 'Q':
                return False
            i += 1
            j += 1
            
            
        i = row
        j = col
        
        while i - 1 >=0 and j + 1 < n:
            if board[i-1][j+1] == 'Q':
                return False
            i -= 1
            j += 1
            
        i = row
        j = col
        
        while i + 1 < n and j - 1 >=0:
            if board[i+1][j-1] == 'Q':
                return False
            i += 1
            j -= 1
            
        
        board[row][col] = 'Q'
        return True
            
        
        
        
        