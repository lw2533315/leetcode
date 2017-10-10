# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        size = len(s)
        b = [""]
        index = 1    #index is the index of b, currently it point to
		#a emply index
        for i in s:
            if index == 1:  #there is nothing in index 1 now, and the "" is
			#the only char in the string
                if i == ")" or i == "}" or i == "]":
                    return False

				#the left brackets can add into the string anytime
                elif i == "(" or i=="{" or i=="[":
                    b.append(i)
                    index += 1
            else:
                if i == "(" or i=="{" or i=="[":
                    b.append(i)
                    index += 1

				#any right bracket when it add into string should checke
				#the left next character, they must be a pair bracket
                if i == ")":
                    if b[index-1] == "(":
                        b.pop()
                        index -= 1
                    else:
                        return False
                if i == "]":
                    if b[index-1] == "[":
                        b.pop()
                        index -= 1
                    else:
                        return False
                if i == "}":
                    if b[index-1] == "{":
                        b.pop()
                        index -= 1
                    else:
                        return False
        if(index == 1):
            return True
        else:
            return False

test = Solution()
print (test.isValid("()"))