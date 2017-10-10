# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
  # [-1,  0, 0, 1],
  # [-2, -1, 1, 2],
  # [-2,  0, 0, 2]
# ]

# 模仿3 sum， 第一第二个数two loop 嵌套，第三，第四个数是最靠近第二个和最后一个开始
# 试探。


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        size = len(nums)
        ret = []

        i = 0
        while  i < (size - 3):

			#i>0,意味着测试完第一个数，那么当第二个...跟前一个相同移动i指针
			#避免重复
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = i + 1
            while j < (size -2):

				#跟i做法一样
                if j > i+1 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                left = j+1
                right = size-1
                while left<right:
                    if nums[i] + nums[j] +nums [left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] <target:
                        left += 1
                    else:
                        ret.append([nums[i],nums[j],nums[left],nums[right]])

						#找到第一组数以后检测下一个数和当前数是否相同相同就移动指针
						#避免出现重复
                        while left<right and nums[left + 1] == nums[left]:
                            left += 1
                        while left<right and nums[right -1] == nums[right]:
                            right -=1
                        left += 1
                        right -= 1


                j += 1

            i += 1


        return ret

test = Solution()
print (test.fourSum([1, 0, -1, 0, -2, 2],0))