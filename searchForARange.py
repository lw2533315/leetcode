# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num = 0      #记录重复的targe次数
        index = 0
        over = True  #检测是否是读完while退出，那么index会比实际大1，需要减掉

        while index < len(nums):
            if nums[index] == target:
                num += 1
            if nums[index] > target:   #检测到term in nums 大于target 跳出
                index -= 1
                over = False
                break
            index += 1

        if over:
            index -= 1

        if num > 0:
            return [index - num +1, index]
        else :
            return [-1,-1]