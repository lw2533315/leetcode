# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.

# Note: Each term of the sequence of integers will be represented as a string.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"

		#1th is 1
        if n == 1:
            return s;


        while n>1:
            index = 0
            counter = 0  #duplicate time
            if len(s)>0:
                c= s[0]
            temp = ""   #new string

            while index < len(s)+1:   #because the last char need to be calculated

                if index < len(s) and c == s[index]:
                    counter += 1
                    index += 1

                else:
                    temp = temp + str(counter) + c   #重复几次几个
					# “1”   ： 1个1  -》11
					# “11”  ： 2个1  -》21
					# "21"  :  1个2 和 1个1  -》1211
					# “1211”:  1个1， 1个2 ， 2个1 -》111221

                    if index == len(s):
                        break
                    c = s[index]    #reset c
                    counter =0		#reset counter


            s = temp

            n -=1
        return s
test = Solution()
print (test.countAndSay(4))
