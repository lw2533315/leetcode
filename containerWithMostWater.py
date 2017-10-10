# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# 面积永远是以两个垂直边里短的那面形成的长方形面积
# 先看最外侧两个，算面积，然后淘汰掉短的那个边往内移动
# 直到不能形成长方形


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        size = len(height)
        max_area = 0
        left_i = 0
        right_i = size-1
        while left_i != right_i:
            if height[left_i] <= height[right_i]:
                temp_area = height[left_i] *(right_i - left_i)
                left_i += 1
                if temp_area > max_area:
                    max_area = temp_area
            else:
                temp_area = height[right_i]*(right_i - left_i)
                right_i -= 1
                if temp_area > max_area:
                    max_area = temp_area

        return max_area