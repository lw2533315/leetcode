# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

# 使用recursive 超时了，有另外一DP方法
#从后面往前面看，

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s_size = len(s)
        if s_size == 0:
            return 0;
        
        
        
        res = [0];  #存储出现的次数
        index = s_size - 1
  
        self.recur(s, index, res)
        
        return res[0]
        
        
    def recur(self, s, index , res):
		#如果index到0，而且值为“0”证明这种分配方法不成立
        if (index == 0 and s[0] != "0") or index == -1: 
            res[0] += 1
        elif index == 0 and s[0] == "0": 
            pass
        else:
            if s[index] != "0":
                self.recur(s, index - 1, res)
            two_bit_val = int(s[index]) + int(s[index - 1]) * 10
            if two_bit_val <= 26 and two_bit_val > 9:
                self.recur(s, index - 2, res)