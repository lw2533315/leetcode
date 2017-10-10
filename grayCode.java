// The gray code is a binary numeral system where two successive values differ in only one bit.

// Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

// For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

// 00 - 0
// 01 - 1
// 11 - 3
// 10 - 2
// My idea is to generate the sequence iteratively. For example, when n=3, we can get the result based on n=2.
// 00,01,11,10 -> (000,001,011,010 ) (110,111,101,100). The middle two numbers only differ at their highest bit, while the rest numbers of part two are exactly symmetric of part one. It is easy to see its correctness.
// Code is simple:
class Solution {
    public List<Integer> grayCode(int n) {
        List<String> list = new ArrayList<>();
        list.add("0");
        list.add("1");
        
        List<Integer> res = new ArrayList<>();
        
        if (n == 0) {
            res.add(0);
            return res;
        }
       
            
       
        while (n > 1) {
			 //保存新生成的字符串集合
             List<String> temp = new ArrayList<>();
            for (int i = 0; i < list.size(); i++)
                temp.add("0" + list.get(i));
            for (int i = list.size() - 1; i >=0; i--)
                temp.add("1" + list.get(i));
            n --;
            list.clear();
            list = temp;
            
        }
        
        //字符串转interger
        for (int i = 0; i < list.size(); i++) {
            res.add(Integer.parseInt(list.get(i), 2));
        }
        
        return res;
        
        
    }
    
    
}