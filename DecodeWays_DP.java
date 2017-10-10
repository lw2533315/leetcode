// DP算法
// 举个例子如果count[i]表示对应S里的第i个字符时可能的组合数，
// 那么当s.charAt(i) > '0' && < '6'  而且s.charAt(i - 1) == '1' or '2'
// 那么 count[i] = count[i - 1] + count[i - 2]  
// s = "121",  count[0] = 1, count[1] = 2
// 那么count[2] = 1 + 2 = 3   可以看成1 补在 “12”后面 的可能性
// 和 21 补在“1” 后面的可能性

class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0)
            return 0;
        
        int s_size = s.length();
        int []count = new int[s_size];
        
        
        //the first two char of s's all situation
        if ( s.charAt(0) == '0' )  //fist char is '0'
                return 0;
        if (s.charAt(0) != '0')
            count[0] = 1;
        
        // _ 0
        if (s_size > 1 && s.charAt(1) == '0')
            // 00,30,40...
            if (s.charAt(0) != '2' && s.charAt(0) != '1')
                return 0;
            else  // 10  or 20
                count[1] = count[0];
        
        // _7, _8, _9
        if (s_size > 1 && s.charAt(1) > '6') {
        //    System.out.println("test 1");
            if (s.charAt(0) != '1')
                count[1] = count[0];
            else //17,18,19
                count[1] = count[0] + 1;
      //      System.out.println ("test 2" + count[1]);
        }
        // 
        if (s_size > 1 && s.charAt(1) <= '6' && s.charAt(1) > '0')
            //11, 21, 12, 22,...16, 26
            if (s.charAt(0) != '2' && s.charAt(0) != '1')
                count[1] = count[0];
            else  // 31,41,....
                count[1] = count[0] + 1;
    
            
        
       
        for (int i = 2; i < s.length(); i++) {
            if (s.charAt(i) == '0')
                if (s.charAt(i -1) == '1' || s.charAt(i -1) == '2')
                    count[i] = count[i - 2];
                else 
                    return 0;
            else{
                if (s.charAt(i) > '6'){
                    if (s.charAt(i -1) != '1') {
                        count[i] = count[i - 1];
                    }
                    else
                        count[i] = count[i - 1] + count[i - 2];
                }
                else {
                    if (s.charAt(i -1) == '1' || s.charAt(i -1) == '2')
                        count[i] = count[i - 1] + count[i - 2];
                    else
                        count[i] = count[i - 1];
                }
            }
            
        }
            return count[s_size - 1];
    }
}