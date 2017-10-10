# Implement int sqrt(int x).
# 找中间值判断把时间压缩到O(logn)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x == 0):
            return 0
        if (x == 1):
            return 1
        
        if x < 0:
            return -1
        
        l = 1; r = x;
        while l < r:
            if r - l > 1:
                m = int((r + l)/2)
                if m** 2 > x:
                    r = m
                elif m** 2 < x:
                    l = m
                else:
                    return m
            else:  #当不能找到中间值了答案不在l就是r
                if l**2 >x:
                    return -1
                if l**2 <= x and r**2 > x:
                    return l
                if r**2 <= x:
                    return r
                
        