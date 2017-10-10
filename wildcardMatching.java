// '?' Matches any single character.
// '*' Matches any sequence of characters (including the empty sequence).

// The matching should cover the entire input string (not partial).

// The function prototype should be:
// bool isMatch(const char *s, const char *p)

// Some examples:
// isMatch("aa","a") → false
// isMatch("aa","aa") → true
// isMatch("aaa","aa") → false
// isMatch("aa", "*") → true
// isMatch("aa", "a*") → true
// isMatch("ab", "?*") → true
// isMatch("aab", "c*a*b") → false
public class Solution {
    public boolean isMatch(String str, String pattern) {
        int s = 0, p = 0, match = 0, starIdx = -1;
        while (s < str.length()){
            // advancing both pointers
            if (p < pattern.length()  && (pattern.charAt(p) == '?' || str.charAt(s) == pattern.charAt(p))){
                s++;
                p++;
            }
            // * found, only advancing pattern pointer
			//记录当前*号位置，记录现在s的位子 把*看成“”开始试探
            else if (p < pattern.length() && pattern.charAt(p) == '*'){
                starIdx = p;
                match = s;
                p++;
            }
           // last pattern pointer was *, advancing string pointer
			//当试探发现后面不符合，并且之前有*，从*号后开始从新试探，s的位置相对上一次往前移动一位
            else if (starIdx != -1){
                p = starIdx + 1;
                match++;  //每次试探 s的index往前移动一位
                s = match;
            }
           //current pattern pointer is not star, last patter pointer was not *
          //characters do not match
		  //不满足上面条件返回false
            else return false;
        }

        //check for remaining characters in pattern
		// s = "aa" p="aa*"类似这种情况s == str.length()
        while (p < pattern.length() && pattern.charAt(p) == '*')
            p++;

        return p == pattern.length();
    }
}