# Divide two integers without using multiplication, division and mod operator.

# If it is overflow, return MAX_INT.

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        quotient = 0

		#overflow 两种情况1.分母为0,2. 214783648越界
        if divisor == 0 or (dividend == -2147483648 and divisor == -1):
            return 2147483647

        if dividend == 0:
            return 0


        #判断正负
        pos = True
        if (dividend >= 0 and divisor < 0 ) or (dividend < 0  and divisor >=0):
            pos = False
        dividend = abs(dividend)
        divisor = abs(divisor)


        #通过左移判断，移动一位就是2倍，两位就是4倍 2^ n
		#一旦发现除数左移大于被除数，将除数右移一位
		#余数赋给被除数，再把除数还原从第一位开始移动
        while dividend >= divisor :
            shif_time = 0
            shif_div = divisor   #除数赋值给临时除数，保留原值
            while dividend >= shif_div:
                shif_div <<= 1
                shif_time += 1
            quotient += 2**(shif_time-1)  #商需要右移一次（幂）一位当前值>被除数
            shif_div >>= 1  #试除数要右移因为实际被剪掉的只是当前除数的一半
            dividend -= shif_div



        if pos:
            return quotient
        else:
            return 0 - quotient