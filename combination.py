// Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

// For example,
// If n = 4 and k = 2, a solution is:

// [
  // [2,4],
  // [3,4],
  // [2,3],
  // [1,2],
  // [1,3],
  // [1,4],
// ]
// 递归， index表示当前的 数字
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        index = 1;
        while index <= n:
            temp = []
            temp.append(index)
            self.recur(res,temp, index+1,k,n);
            index += 1
        return res
        
        
    def recur(self,res,temp, index, k, n):
       
        if len(temp) == k:
            res.append(temp)
            return
        else:
            while index <= n:
                temp_t = [];
                temp_t = temp[:]
                temp_t.append(index)
                self.recur(res, temp_t, index + 1,k,n)
                index += 1
        