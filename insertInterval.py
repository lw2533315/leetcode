# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# 先按照Interval.start排序，

Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        if newInterval == []:
            return intervals;
        
        res = []
        
        if len(intervals) == 0:
            res.append(newInterval)
            return res
        
        #sort intervals by Interval.start
        intervals_sort = sorted(intervals, key = lambda x:x.start)
        
        s = newInterval.start
        e = newInterval.end
        
        for i in range (len(intervals_sort)):
            #插入的item 在当前item右侧
            if s > intervals_sort[i].end:
             
                res.append(intervals_sort[i])
                
            #插入的item在当前item左侧
            elif e < intervals_sort[i].start:
             
                res.append(Interval(s,e))
                s = intervals_sort[i].start
                e = intervals_sort[i].end
            
            #当前item在要插入的item 内部
            elif e>= intervals_sort[i].end and s <= intervals_sort[i].start:
                pass
                
           
            else:
                # [0,0][1,4][6,7 ]   new = [2, 5]   -> new = [1, 5]
                if s >= intervals_sort[i].start and s <= intervals_sort[i].end:
                 
                    s = intervals_sort[i].start
                    e = max(e, intervals_sort[i].end)
                    
                # [[6,7]]    new = [3,9]    -> new [3,]
                else:
                           
                    e = intervals_sort[i].end
                    s = min(s, intervals_sort[i].start)
            
            
            
        res.append(Interval(s,e))
        
        return res
                
        
                
        
        