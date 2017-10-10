// Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

// For example,
// S = "ADOBECODEBANC"
// T = "ABC"
// Minimum window is "BANC".

// 需要两个指针来限定window的边界(l,r)，移动r指针将substring扩大，判断是否包含
// t， 当找到一个合适的substring包含t后，记录下来，然后分别向右
// 移动r 和 l，然后进行新的判断

class Solution {
    public String minWindow(String s, String t) {
        String res = s;
        int  l = 0, r = 0;
        
        if (t.length() > s.length())
            return "";
		
		//记录s的l和r之间的字符串包含的对应t中字符出现的次数
		//可以用map
        int has_found [] = new int [256];
		//遍历t来记录每个字符出现的次数，可以
		// 用map来代替
        int need_found[] = new int [256]; 
		
		//遍历t
        for (int i = 0; i < t.length(); i++){
            //System.out.println("char is " +t.charAt(i));
            need_found[t.charAt(i)] ++;
            
        }
        
		//用来记录s中真正有小的字符数，即是t中的字符
        int temp_need = t.length();  
        boolean has_win = false;  
        for (; r < s.length(); ){
            //当前s的char没有在t中找到, 看下一个char
            if (t.indexOf(s.charAt(r)) == -1 ){
                r += 1;
            }
            else {
                //找到t中的字符，在has_found记录
                has_found[s.charAt(r)] ++;
                
                //只有当has_found对应的item的value小于need_found时，当前找到的才能满足当前需要，不然
                //只能存着为将来用
                if (has_found[s.charAt(r)] <= need_found[s.charAt(r)]){
                    temp_need -- ;  //需求减 1
                }
									
                r += 1;
				
				//当需求为0 时
                if (temp_need == 0){
                    has_win = true; //设置找到合适的substring
					
					//找到包含t的substring后需要判断l是否可以右移得到更小的substring
					//1.如果l对应的字符不在t里面，右移
				//2.如果l对应的字符在t里，同时has_found[这个字符] > need_found[这个字符]
				//那么右移，修改has_found. eg: s = "abcbd" t= "bd"
				//当 l == 0，r = 4， a不再t里 l++， 然后l指向b，has_found['b'] == 2 大于need_found,所以b再
				//右移修改 has_found
				
                    while (t.indexOf(s.charAt(l)) == -1 || has_found[s.charAt(l)] > need_found[s.charAt(l)]){
                        has_found[s.charAt(l)] --;
                        l += 1;
                    }
                   
                    if (r - l < res.length()){
                        res = s.substring(l, r);
                    }
					
					//取完 substring后，左指针需要右移
                    has_found[s.charAt(l)] -- ; 
					
                    //s = "abcda",    t = "ac"   l = 0, r = 2,  substring: abc 如果l右移那么a不再在新substring：bc里，所以需要增加
                    if (has_found[s.charAt(l)] < need_found[s.charAt(l)]) //左指针右移如果substring不能包含t，那么需要增加 
                        temp_need ++;
                    l += 1;
                    
                }
            }
        }
        
        
        
        if (has_win == false){
        
            return "";
        }
        return res;
        
    }
}