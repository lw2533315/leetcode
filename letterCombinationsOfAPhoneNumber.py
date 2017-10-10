# Given a digit string, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below.



# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

# 每次读取一个数字与之前已经组合的数字进行组合  o(n^3)

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """


        dig_to_str = {'0' : "", '1':"",'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        size = len(digits)

        #input is ""
        if size == 0:
            return []

        ret = [""]

        for i in range(size):
            print("digits",digits[i])

            #临时存放生成的新的list，
            temp = []

            s = dig_to_str[digits[i]]# 得到数字对应的字符串

			#该字符串与之前形成的list 组合生成新的list
			for j in s:
                print("j is ",j)
                for k in range(len(ret)):
                    temp.append(ret[k] + j)
            print (ret)
            ret = temp  #讲新的list赋值给return list
            print ("temp is ", temp)



        return ret



test = Solution()
print(test.letterCombinations("22"))