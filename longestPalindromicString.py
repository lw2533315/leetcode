# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
# Example:

# Input: "cbbd"

# Output: "bb"








class Solution(object):
    start = -1

    longest = -1
    def findLongest(self, s,j,k):
        #both side of the center is same
        while j>=0 and k<len(s) and s[j] == s[k]:
            j-=1
            k+=1

        if (self.longest < k -j -1):
            self.longest = k - j -1
            self.start = j+1



    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size == 0:
            return ""
        if size == 1:
            return s[0]
        for index in range (size):
            self.findLongest(s,index,index)    #size of the string is odd
            self.findLongest(s,index,index+1)  #even

        return s[self.start:self.start+self.longest]