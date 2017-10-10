# Given a collection of integers that might contain duplicates, nums, return all possible subsets.

# Note: The solution set must not contain duplicate subsets.

# For example,
# If nums = [1,2,2], a solution is:

# [
  # [2],
  # [1],
  # [1,2,2],
  # [2,2],
  # [1,2],
  # []
# ]

# 通过while + recursive 实现组合的各种可能性，因为nums中
# 有重复元素，所以最后排序以后遍历一遍把重复的删除

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = [];
               
        temp = []
        nums = sorted(nums)
        self.recur(0, nums, res, temp)
        
		#删除重复项
        res = sorted(res)
        i = 0
        while i < len(res):
            if i + 1 < len(res) and res[i] == res[i + 1]:
                del res[i]
            else:
                i += 1
            
        
        return res
        
    def recur(self, index, nums, res, temp):
        res.append(temp);
  
        while index < len(nums):
            temp_while = temp[:]  #深度复制让temp在各个recursive中不会相互干扰
            temp.append(nums[index])
            self.recur(index + 1, nums, res, temp_while)
            index += 1
        
        
       
            
        
        