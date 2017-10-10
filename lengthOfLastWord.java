// Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

// If the last word does not exist, return 0.

// Note: A word is defined as a character sequence consists of non-space characters only.

// For example, 
// Given s = "Hello World",
// return 5.

class Solution {
    public int lengthOfLastWord(String s) {
        if ( s.length() == 0)   //空字符串
            return 0;
        int index = s.length() - 1;
        while (index >=0 && s.charAt(index) == ' ')   //把结尾连续的‘ ’字符去掉
            index --;
        int count = 0;
        if (index < 0 )
            return 0;

        
        for ( ; index >=0; index -- ){
            if (s.charAt(index) != ' ')
                count += 1;
            else{
               break;
                }
        }
        return count;
    }
}