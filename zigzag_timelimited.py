class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        size = len(s);
        two_d = []
        if size == 0:
            return ""
        
        for i in range(numRows):
            two_d.append([])
            
        i = 0
        while i < size:
        
            for j in range(numRows):
                if i < size:
                    print ("````` j is ", j ,"value is ",s[i])
                    two_d[j].append(s[i])
                    i += 1
                else:
                    break
            for j in range(numRows-2, -1,-1):
                print("j is ",j)
                if i < size:
                    print ("s value is ", s[i])
                    two_d[j].append(s[i])
                    i += 1
                else:
                    break
        
        ret = ""
        print ("numRows is ",numRows)
        for k in range(numRows):
            
            for l in range(len(two_d[k])):
                ret += two_d[k][l]
        return ret
test = Solution()
print(test.convert("ABCD",2))
