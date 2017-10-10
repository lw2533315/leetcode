# The set [1,2,3,…,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.

# 我的方法从高位到低位逐位确定数字。

# 以图例n=3进行说明：

# 构建数组v={1,2,3}

# 确定最高位：

# index=(k-1)/2

# 注：分母2是指每个最高位持续的排列数。由于除了最高位之外还有n-1=2位，一共可以出现2!种排列。

# index指的是所求的第k个排列会落在哪一个最高位的覆盖范围内。

# k==1,2时，index==0，最高位为v[index]==1

# k==3,4时，index==1，最高位为v[index]==2

# k==5,6时，index==2，最高位为v[index]==3

# 其余数位如上思路逐位确定。

# 注意：

# 1、k的更新。

# 2、s的更新 没有用到的1-n 之间的数，按照从小到大的顺序



class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        leng = 1
        s = []   #s 存了从1，开始到n的所有数字，下标分别比他们的值少1
        while leng <= n:
            s.append(leng)
            leng += 1
        
        res = []
        while n > 0:
            
            # n =2 时 
            #12
            #21
            # s = [1,2]
            # k如果是2 , 那么index 应该是0  
            index = (k-1) / math.factorial(n - 1)
            res.append(str(s[index]))
            del s[index]
            k -= index*math.factorial(n-1)    //剩余的，不能取mod，k不是从0开始
            n -= 1
                       
        return "".join(res)