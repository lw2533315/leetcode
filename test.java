
import java.util.*;
import java.lang;

class Solution {
	public static boolean  isMatch(String s, String p) {
		int i = 0;
		int j = 0;
		int s_size = s.length();
		int p_size = p.length();

		//两个字符串都是空
		if(s_size == 0 && p_size == 0)
			return true;

		if(s_size == 0 && p.equals("*"))
			return true;

		if (s_size == 0 && !p.equals("*"))
			return false;

		if(s_size !=0 && p_size == 0)
			return false;

		if(s.charAt(s_size-1) != p.charAt(p_size-1) && p.charAt(p_size-1) != '?' && p.charAt(p_size-1) != '*')
			return false;


		List<String> list = new ArrayList<>();
		recur(s,p,i,j,list);
		for(String x: list) {
			if(x == "t")
				return true;
		}

		return false;



	}
	public static void  recur(String s, String p, int i, int j, List<String> list) {
		//已经找到一个true
		if (list.lastIndexOf("t") != -1)
			return ;

		//无效的j，j已经知道end（）位子
		if ( j == p.length()) {
			list.add("f");
			return;
		}

		//发现连续的*，跳过
		if (p.charAt(j) == '*' && j < p.length()-1 && p.charAt(j+1) == '*') {
			recur(s,p,i,j+1,list);
			return;
		}


		//s 已经指向end（），p 最后一个char是*
		if (i == s.length() && p.charAt(j)== '*' && j == p.length() - 1 ) {
			list.add("t");
			return ;
		}
		//p最后一个不是* s指向end（）
		if (i == s.length()) {
			list.add("f");
			return;
		}

		//两个字符串对应的字符不相同，p的不为？或者* 返回false
		if (s.charAt(i) != p.charAt(j) && p.charAt(j) != '?' && p.charAt(j) != '*') {
			list.add("f");
			return;
		}

		//i,j 都是字符串最后一个，并且相同或者一个为？或者一个为*，返回true
		if (i == s.length()-1 && j == p.length()-1 && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?' || p.charAt(j) == '*')) {
			list.add("t");
			return;
		}

		//不为最后一个char，但是相同
		if (s.charAt(i) == p.charAt(j))
			recur(s,p,i+1,j+1,list);

//j不是最后一个并且j为？
		if (p.charAt(j) == '?') {
			recur(s,p,i+1,j+1,list);
		}

		//不是最后但是p为*
		if (p.charAt(j) == '*') {


			recur(s,p,i,j+1,list);   //* 看成空字符
			recur(s,p,i+1,j,list);      //*看成长度超过1的字符串
			recur(s,p,i+1,j+1,list);    //* 看成1个字符

		}
	}

	public static void main(String[] args) {
		String s = "";
		String p = "*";
		if (isMatch(s,p))
			System.out.println("is match");
		else
			System.out.println("is not match");

	}
}