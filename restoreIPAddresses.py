# Given a string containing only digits, restore it by returning all possible valid IP address combinations.

# For example:
# Given "25525511135",

# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

# 可以是0开头，但是不能01. 这个样子  eg 0.0.1.1  可以，但是0.01.1.1 不行
# .255.  可以 .256.不行
# 用recursive 组合
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        s_size = len(s)
        res = []
        if len(s) == 0:
            return res
        
    
        dot_c = 0 # dot number
        if s[0] == '0':
            self.recur(s, dot_c, 1, res)
		#字符串不是0开头，那么小数点可以在index 1,2,3
        else:
            index = 1
            while index < len(s) and index <= 3:
				#如果小数点在index 3，那么. 前面的三个char不能大于255
                if index == 3 and int(s[0]) * 100 + int(s[1])* 10 + int(s[2]) > 255:
                    break
                self.recur(s, dot_c, index, res)
                index += 1
        return res
        
    def recur(self, temp , dot_c, dot_index, res):
		#把小数点加到字符串里
        temp = temp[0:dot_index] + "." + temp[dot_index:]
        dot_c += 1
      
        #跳出recursive条件
        #3个点，并且剩下的长度在1-3
        if dot_c ==3 and (len(temp) - dot_index <= 4 and len(temp) - dot_index > 1):
         
            if temp[dot_index + 1] == '0': 
                if dot_index + 2 == len(temp): #点后面是0的话，只能有1位 
                    res.append(temp)
                else:
                    return
            else:
				#最后的. 后面有3个数要判断大小
                if len(temp) - dot_index == 4 and int(temp[dot_index +1]) * 100 + int (temp[dot_index + 2]) * 10 + int(temp[dot_index +3]) > 255:
                    return
                else:
                    res.append(temp)
		
		#当有1个点，两个点，3个点的跳出条件
        if len(temp) - dot_index >4 and dot_c == 3:
            return
        elif len(temp) - dot_index > 7 and dot_c == 2:
            return
        elif len(temp) - dot_index > 10  and dot_c == 1:
            return
        elif len(temp) - dot_index > 13 and dot_c == 0:
            return
        
        #下一个.的起始位置，中间最少间隔一个字符，所以是加2
		dot_index += 2
      
        
        #检测上一个 . 后面是0还是其他数值
        zero_first = False
        if (dot_index < len(temp) and temp[dot_index - 1] == '0'):
            zero_first = True;
        #只需要3次因为ip 每两点中间最多3个数字
        counter = 1;
        while dot_index < len(temp) and counter <= 3 :
			
			#当两个点间隔达到3，要判断数值大小
            if counter == 3 and int(temp[dot_index - 3]) * 100 + int (temp[dot_index - 2]) * 10 + int(temp[dot_index - 1]) > 255:
                break;
            
            self.recur(temp, dot_c, dot_index,  res)
            
            if zero_first:  #如果上一个.后面是0，那只有一种recursive调用情况就是.紧跟0
                break;
            
            dot_index += 1
            
            counter += 1
            
        