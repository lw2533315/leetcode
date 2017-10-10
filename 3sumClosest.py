class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        size = len(nums)
        sum_3 = 0     # return value
        close_target = 2**31 -1   #the distance between sum and target
        
        
        for i in range(size):
            j = i + 1;
            k = size -1 
            while(j < k):
                sum_temp = nums[i] + nums[j] + nums[k]
               
                if sum_temp - target > 0:
                   
                    temp = abs(sum_temp - target)       #sum is greater than target
                   
                    if (temp < close_target):           #newer distance is smaller than older distance update distance and return value
                        close_target = temp             
                        sum_3 = sum_temp
                    k -= 1                              #sum decrease
                elif sum_temp - target < 0:
                   
                    temp = abs(sum_temp - target)
                    if (temp < close_target):
                        close_target = temp
                        sum_3 = sum_temp
                    j += 1
                else:
                    return target
        return sum_3
                
                
           
test = Solution()
print(test.threeSumClosest([1,1,1,1], -100))
