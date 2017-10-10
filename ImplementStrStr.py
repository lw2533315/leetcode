# Implement strStr().

# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        if haystack == "":
            return -1

        size_needle = len(needle)
        size_hay = len(haystack)

        if size_needle > size_hay: #substr 长过str
            return -1

        index = 0

        while index < size_hay:

            if size_hay - index < size_needle:  #剩余的str部分没有needle长
                return -1

			#在for 中同样要同步测试haystack， 但是又不能修改index只能通过改变n移动
			n = 0

            for j in range(size_needle):

                if (haystack[index+n] != needle[j]):
                    break
                if j == size_needle-1: #检测通过了最后一个char of needle
                    return index
                n += 1
            index += 1
        return -1


test = Solution()
print (test.strStr("aaaa","aa"))