# Given a collection of intervals, merge all overlapping intervals.

# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# 主要是对原有的list 按照intervals的start的排序
# 减少需要判断的情况

Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) <= 1:
            return intervals
        res = []
        dic = {}


        #按照s对list排序
        i_s = sorted(intervals, key = lambda x:x.start)

        s = i_s[0].start
        e = i_s[0].end

        for i in range (1,len(i_s)):

			#如果前面的e>=后面的s，证明是连贯的
            if e >= i_s[i].start:
                e = max(i_s[i].end,e)  #取最大范围

            else:

                temp = Interval(s,e);
                res.append(temp)
                s = i_s[i].start
                e = i_s[i].end

		#最后一个item要加入到res
        temp = Interval(s,e)
        res.append(temp)

        return res


