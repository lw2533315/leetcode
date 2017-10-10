# Validate if a given string is numeric.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
# 首先去掉前后的空格，然后对于 "."进行判断，然后去掉开头的+/-
# 通过e和.对情况进行分类，然后通过去掉e，.进行判断
 class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()  #去除开头结尾的所有 ' '
        
        
        
        if len(s) == 0:
            return False
        
        
               
        if s[0] == '-' or s[0] == '+':#去掉正负号
            s = s[1:]
        
        if s[0] == '.' and len(s) == 1: #'.'
            return False
        
        
        e_index = s.find("e")
        p_index = s.find(".")
        
        #没e，没.
        if e_index == -1 and p_index == -1:
            for i in range(len(s)):
                if (s[i] < '0' or s[i] >'9'):
                    return False
            return True
        
        #有e
        if e_index != -1 and p_index == -1:
            if e_index == 0 or e_index == len(s) - 1:  #e开头e结尾都不对
                return False
            if s.find("e", e_index + 1) != -1:    #发现第二个e 不对
                return False
            
            if e_index + 2 < len(s) and (s[e_index+1] == '+' or s[e_index+1] == '-'): #去掉e后面的+ or -
                s = s[0:e_index + 1] + s[e_index + 2:]
            s = s[0:e_index] + s[e_index + 1:]
            for i in range(len(s)):
                if (s[i] < '0' or s[i] >'9'):
                    return False
            return True
        
        #有.
        if e_index == -1 and p_index != -1:
            if s.find(".", p_index + 1) != -1:
                return False
            s = s[0:p_index] + s[p_index + 1:]
            for i in range(len(s)):
                if (s[i] < '0' or s[i] >'9'):
                    return False
            return True
        
        if e_index != -1 and p_index != -1:
            if e_index == 0 or e_index == len(s) - 1:
                return False
            if s.find("e", e_index + 1) != -1:  #查找重复的e 
                return False
            if s.find(".", p_index + 1) != -1:  #查找重复的.
                return False
            if e_index < p_index:           #e后面不可能有.
                return False
            if p_index == 0 and e_index - p_index == 1: # .e
                return False              
            if e_index + 2 < len(s) and (s[e_index+1] == '+' or s[e_index+1] == '-'): #去掉e后面的+ or -
                s = s[0:e_index + 1] + s[e_index + 2:]
            
            s = s[:p_index]+s[p_index+1:e_index]+ s[e_index+1: ]
            print (s)
            for i in range(len(s)):
                if (s[i] < '0' or s[i] >'9'):
                    return False
            return True
            
        