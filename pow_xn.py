 # Pick One
# Implement pow(x, n).

#用递归实现pow(x,n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if x == 0:
            return 0


        if n == 0:
            return 1
        if n < 0:
            x = 1/x;
            n = -n;


		#直接递归会超过递归深度 深度在1000左右（stack 只能放那么多）
		#所以不能 if n > 0:
		#			  return x*self.myPow(x,n-1)
        if n%2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x*self.myPow(x*x, n/2)


		# p(x,5)
		# 5>0 5%2 =1
		# return x*p(x^2, 5/2 = 2)
		# x*p(x^2,2)
		# 2>0, 2%2 =0
		# return x*p(x^4,2/2 =1)
		# x*p(x^4,1)
		# 1>0  1%0 = 1
		# return x*x^4*p(x^8,0)
		# x^5*1 = x^5

