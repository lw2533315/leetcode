class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        size = len(s)


        #只有当left == right 当前点之前的括号才能全部匹配
		#记录下当前这次试探的长度比较最长的substr
        left = 0
        right = 0
        counter = 0  #记录加了多少个括号
        longest = 0  #left == right
        for j in range(size):
            if size - j <= longest:
                break

            index = j
            while index < size:
                if s[index] == '(':
                    left += 1
                    counter += 1
                elif left > right and s[index] == ')':
                    right += 1
                    counter += 1
                    if left == right:
                        if longest < counter:
                            longest = counter
                else:
                    break

                index += 1
            left = 0
            right = 0
            counter = 0

        return longest