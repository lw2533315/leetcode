# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
  # ["ate", "eat","tea"],
  # ["nat","tan"],
  # ["bat"]
# ]

//对于同样字符组成的不同words要判断是否一样需要对每个string 排序
//排序的同时可以把排序后的字符串作为key，利用不可重复的特性把所有排序后
//形成同一个word的字符串放在该key的value里（value是一个集合）
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        res = []
        dic = {}
        index  = 0   #index in strs
		
		//把排序后的字符串作为key， 
        for index in range (len(strs)):
            temp = "".join(sorted(strs[index]))
            
            if  temp not in dic:  //需要把key的value定义为一个集合
                dic[temp] = [];
                
            dic[temp].append(strs[index])  //排序后相同的字符串在一个key的value里
        
		for k in dic:
            res.append(dic[k])
        
       
        return res