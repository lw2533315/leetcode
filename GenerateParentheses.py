

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
  # "((()))",
  # "(()())",
  # "(())()",
  # "()(())",
  # "()()()"
# ]


class Solution(object):
    ret = []

    def recur(self,temp, left, right, n):
        if len(temp) == n*2:
            self.ret.append(temp)

		#注意left，right 等变量都是在做参数时才改变，不会影响
		#recursive之前的变量
        if (left < n):
            self.recur(temp+"(", left+1,right,n)
        if (right < left):
            self.recur(temp+")", left, right +1, n)


    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.recur("",0, 0,n)

        return self.ret

test = Solution()
print (test.generateParenthesis(1))
