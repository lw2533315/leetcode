# “ABCDEF”， 3
# A E           A   E
# BDF    -》     B D F
# C               C 


# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string text, int nRows);



class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s)
        print ("size is ", size)

        if size == 1:
            return s[0]
        if size == 0:
            return ""
        
        if numRows ==1 :   #只在一行上
            return s

        #建立2d array
        two_d = []
        for i in range(numRows):
            two_d.append([])

            

        #index = 1
        #two_d[0].append(s[0])
        ceiling = True;  #设定标记判断是在0行还是numRows - 1行
        for i in range (size): 
            if i % (numRows -1) == 0:
                if ceiling:    
                    two_d[0].append(s[i])
                    ceiling = False    #离开0行
                else:
                    two_d[numRows-1].append(s[i])
                    ceiling = True     #转向0行
            else:
                if not ceiling: #离开0行后直接% 求row
                    two_d[i % (numRows - 1)].append(s[i])
                else:           #向0行需要用最大行下标- %
                    two_d[numRows-1-(i%(numRows - 1))].append(s[i])
        ret = ""
        for i in range(numRows):
            for j in two_d[i]:
                ret += j

        return ret
           
test = Solution()
print(test.convert("ABCD",2))
