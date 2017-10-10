# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

    # great
   # /    \
  # gr    eat
 # / \    /  \
# g   r  e   at
           # / \
          # a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    # rgeat
   # /    \
  # rg    eat
 # / \    /  \
# r   g  e   at
           # / \
          # a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    # rgtae
   # /    \
  # rg    tae
 # / \    /  \
# r   g  ta  e
       # / \
      # t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
		#终止条件是最终分割以后
        if s1 == s2:
            return True;
			
		#s1 可以不等于s2，但是他们包含的字符要一致
        m = {}
        
        for v in s1:
            if v not in m:
                m[v] = 1
            else:
                m[v] += 1
            
        for v in s2:
            if v not in m:
                return False;
            else:
                m[v] -= 1
            
        for v in m:
            if m[v] != 0:
                return False
        
        print ("test 1")
        index = 1  #必须从1开始
		
		#只要找到一个true的解就返回true
        while index < len(s1):
			#两个字符串分割点前面为乱序，并且后面也为乱序 #或者对于分割点一个字符串的前面部分和另一个字符串的
			#后面部分是乱序并且一个字符串的后面部分和另一个字符串的
			#前部分是乱序。那么整个字符串就是乱序
			
            if (self.isScramble(s1[0:index], s2[0:index]) and self.isScramble(s1[index:len(s1)],s2[index:len(s1)])) or (self.isScramble(s1[0:index], s2[-index:]) and self.isScramble(s1[index:], s2[:-index])):
                return True;
            index += 1
        
        return False
                    