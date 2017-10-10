class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        test = []
        if len(word) == 0:
            return True
        for i in range (len(board)):
            for j in range (len(board[0])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True;
                    
                    if self.find(board,i,j,word,0):
                        return True
        return False
        
    def find(self, board,row,col, word,index):  #board[row][col] == word[index] 才调用这个函数
       
        board[row][col] = ' ';
        if index == len(word) - 1:
            #print "treu！！！！！！！！！！"
            return True
        else:
            
            if row + 1 < len(board) and board[row + 1][col] == word[index + 1]:
				#必须要判断，应为我只要返回的true值，无论返回多少个False
				#只要一个true就可以了，所以这里要判断而不是直接return
				#一条路径不通，还要测试其他可能的路径，如果直接return
				#后面的if 路径就不会测试了
                if self.find(board, row + 1, col, word, index + 1):
                    return True;
            if row - 1 >= 0 and board[row - 1][col] == word[index + 1]:
                if self.find(board, row -1 ,col,word, index + 1):
                    return True
            if col + 1 < len(board[0])and board[row][col+1] == word[index + 1]:
                if self.find(board, row, col + 1, word, index +1):
                    return True
            if col - 1 >= 0 and board[row][col-1] == word[index + 1]:
                if self.find(board, row, col -1, word, index + 1):
                    return True
        
		#不要忘记把不合适的路劲上的所有grid值修改回来
        board[row][col] = word[index]
        return False
                
        
                
            