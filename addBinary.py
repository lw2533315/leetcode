# Given two binary strings, return their sum (also a binary string).

# For example,
# a = "11"
# b = "1"
# Return "100".



class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a_size = len(a)
        b_size = len(b)
       
       #补齐两个字符串 
        if a_size > b_size:
            zero_n = a_size - b_size
            temp = "0" * zero_n
            b = temp + b
                
        elif a_size < b_size:
            zero_n = b_size - a_size
            temp = "0" * zero_n
            a = temp + a
        
		#字符串转list
        a_l = list(a)
        b_l = list(b)
		
		#生成返回的list
        res = ['0']*(len(a_l)+1)
        index = len(a) - 1
      
        carry =  0
        while index >= 0:
            
			#char->int直接换，不用ascii码表char - ’0‘
            if int(a[index]) + int(b[index]) + carry == 2:
              
                res[index + 1] = '0'
                carry = 1
            elif int(a[index]) + int(b[index]) + carry == 1:
              
                carry =  0
                res[index + 1] = '1'
            elif int(a[index]) + int(b[index]) + carry == 3:
              
                res[index + 1] = '1'
                carry = 1
            else:
              
                carry = 0
                res[index + 1] = '0'
            index -= 1
        
        if carry == 1:
            res[0] = '1'
            return "".join(res)
        else:
            return "".join(res[1:])
                