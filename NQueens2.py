

# Follow up for N-Queens problem.

# Now, instead outputting board configurations, return the total number of distinct solutions.


#基本做法同NQueens

class Solution(object):
    
    
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        
   
        count = [0]; 	#记录返回值的参数，因为要作为函数recur的一个参数，数字
						#在参数里是不能更改的，所以用list的第一个元素来存储
        board = []
        for i in range(n):
            board.append([])
        for i in range (n):
            for j in range(n):
                board[i].append('.')
        
        self.recur(0,board,count,n)
        return count[0]
        
        
    def recur(self, row, board, count,n):
        if row == n:
             
            count[0] += 1
          
            
            return 
        for col in range(n):
            if self.is_valid(row, col, board, n):
                self.recur(row+1, board, count, n)
                board[row][col] = '.'
                
        
        
    def is_valid(self, row, col, board,n ):
        
        board[row][col] = '.'
         #check col
        for val in board:
            if val[col] == 'Q':
                return False
        #check row
        for i in range (n):
            if board[row][i] == 'Q':
                return False
        
        #check left up
        i = row
        j = col
        while i - 1>=0 and j - 1 >=0:
            if board[i-1][j-1] == 'Q':
                return False
            i -= 1
            j -= 1
        
        #check right up
        i = row
        j = col
        while i - 1>=0 and j + 1 < n:
            if board[i-1][j+1] == 'Q':
                return False
            i -= 1
            j += 1
            
         #check left down
        i = row
        j = col
        while i + 1 < n and j - 1 >=0:
            if board[i+1][j-1] == 'Q':
                return False
            i += 1
            j -= 1
        
        #check right down
        i = row
        j = col
        while i + 1 < n  and j + 1 < n:
            if board[i+1][j+1] == 'Q':
                return False
            i += 1
            j += 1
        board[row][col] = 'Q'
        return True