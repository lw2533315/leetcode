# Given a set of distinct integers, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,3], a solution is:

# [
  # [3],
  # [1],
  # [2],
  # [1,2,3],
  # [1,3],
  # [2,3],
  # [1,2],
  # []
# ]

# 本题很大部分代码来自 combination， 唯一不同是k是从0 到len（nums）的所有数
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums_size = len(nums)
        res = []
        res.append([])
		
		#len(nums) == 0 || 1 的特殊情况
        if nums_size == 0:
            return res
        temp = []
        if nums_size == 1:
      
            res.append(nums)
            return res
     
		#把k = 1 和k= len（nums）的情况先加入到res里
        for v in nums:
            res.append([v])
            temp.append(v)
        res.append(temp)
        
        k = 2
        
        while k < nums_size:
			#这里开始是调用combination里面的方法了
            self.combine(res,nums,k)
            k += 1
        return res
    def combine(self,res, nums, k):
           
        index = 0;
        
        while index < len(nums):
           
            temp = []
            temp.append(nums[index])
            self.recur(res,temp, index+1,k,nums);
            index += 1
        
        
        
    def recur(self,res,temp, index, k, n):
      
        if len(temp) == k:
            res.append(temp)
            return
        else:
            while index <len(n):
                temp_t = [];
                temp_t = temp[:]
                temp_t.append(n[index])
                self.recur(res, temp_t, index + 1,k,n)
                index += 1
                
