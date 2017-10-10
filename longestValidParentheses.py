
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        valid_t = []
        longest = 0
        size = len(s)

        index  = 0 ;
        while index < size:


            #当前是 (
            if s[index] == '(':
                valid_t.append(0)

            #当前是 ）
            else:
                #之前一位不存在，当前是第一个字符
                if index-1 < 0:
                    valid_t.append(0)

                else:

                    #当前是 ）并且之前是 （
                    if s[index-1] == '(':

                        #之前两位存在
                        if index - 1 -1 >=0:
                            temp = 2 + valid_t[index-2]
                            valid_t.append(temp)

                            if temp > longest:
                                longest = temp

                        else:
                            valid_t.append(2)

                            if 2 > longest:
                                longest =  2
                    #当前是 ）之前是 ） 需要读取之前 ')'对应的valid_t的数值然后往前移对应的位置检测它之前的对应的valide_t的值
                    else:
                        print ("7")
                        temp =  index -1 - valid_t[index-1]
                        if temp >=0 and s[temp] == '(':
                            if temp == 0:
                                valid_t.append(2 + valid_t[index-1])

                            else:
                                valid_t.append(2 + valid_t[index-1] + valid_t[temp-1])

                            if valid_t[index] >longest:
                                longest = valid_t[index]
                        #对应的是  ） 不符合要求
                        else:
                            valid_t.append(0)



            index += 1
        return longest