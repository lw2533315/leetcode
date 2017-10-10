// Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

// You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

// Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

// For the last line of text, it should be left justified and no extra space is inserted between words.

// For example,
// words: ["This", "is", "an", "example", "of", "text", "justification."]
// L: 16.

// Return the formatted lines as:
// [
   // "This    is    an",
   // "example  of text",
   // "justification.  "
// ]
// Note: Each word is guaranteed not to exceed L in length.
// 给一个字符串数组，然后给了需要返回的容器内字符串的宽度。容器内每行尽可能多的
// 读入words数组中的字符串，已经放入的让字符串之间的间隔尽可能相等，多于部分从第一个
// 间隔开始放 eg 4 个字符串之间有3个间隔，如果需要填充5个“ ”， 那么每个间隔填1，多于的
// 从第一个间隔补充起 那么每个间隔分别填入 2，2，1 个 “ ”。 最后一行把“ ”都留在字符串末尾
// 很多字符串操作用StringBuffer

class Solution {
	public List<String> fullJustify(String[] words, int maxWidth) {
		int len_sum = 0;   //recorder the lenth 帮助判断是否一行还能放得下
		int distance = 0; //两个words之间的分配距离
		int mod = 0;//不能等分的多余距离
		List<String> temp = new ArrayList<>(); //temp save the word from words
		List<String> res = new ArrayList<>();




		for(int i = 0; i<words.length;) {
			
			//讲判定出的每组字符串放入temp容器
			if (len_sum + words[i].length() <= maxWidth) { //放在最后可以不用空格
				len_sum += (words[i].length() + 1); //可能需要往后面加word，要预留“ "作为两个单词之间分隔
				temp.add(words[i]);
				i ++;
			
			//发现放不下对temp里的字符串进行处理
			} else {
				StringBuffer sb = new StringBuffer();

				len_sum = 0; //reset
				int len = 0; //the total length of word in temp
				int temp_size = temp.size();
				
				//求出当前行的所有单词的长度，没有空格
				for(int j = 0; j< temp_size; j++) {
					len += temp.get(j).length();
				}

				//  int distance = 0; //两个words之间的分配距离
				// int mod = 0;//不能等分的多余距离
				int left = maxWidth - len;
				
				//如果只有一个单词的情况，所有空格都放在单词后面
				if (temp_size == 1) {
					distance = left;
					sb.append(temp.get(0));
					for(int k =0; k<distance; k++)
						sb.append(" ");

				} else {
					distance = left / (temp_size - 1); //能均匀分配的空格
					mod = left % (temp_size - 1);   //多出来的不能均匀分配的空格


					for(int j = 0; j<temp_size; j++) {
						sb.append(temp.get(j));
						
						//非本行最后一个单词才需要在单词后加上空格
						if (j != temp_size - 1) {
							for(int k = 0; k<distance; k++)
								sb.append(" ");
							//每补充一个非均匀分配空格，总数减少1
							if (mod > 0) {
								sb.append(" ");
								mod -= 1;
							}
						}
					}

				}
				temp.clear();   //reset temp
				res.add(sb.toString());
			}
		}
		
		//最后一组在temp中因为i++ 已经跳出循环
		if (!temp.isEmpty()) {
			StringBuffer sb = new StringBuffer();

			len_sum = 0; //reset
			int len = 0; //the total length of word in temp
			int temp_size = temp.size();
			for(int j = 0; j< temp_size; j++) {
				len += temp.get(j).length();
			}

			//  int distance = 0; //两个words之间的分配距离
			// int mod = 0;//不能等分的多余距离
			int left = maxWidth - len;


			for(int j = 0; j<temp_size; j++) {
				System.out.println("last group sb size is" + sb.length());
				sb.append(temp.get(j));
				if (left - j - 1 >= 0)
					sb.append(" ");
			}
			System.out.println(" left is "+left);
			System.out.println("sb is "+sb+" size is "+sb.length());

			left =maxWidth - sb.length();
			System.out.println("left space is  "+left);
			for(int k = 0; k<left; k++)
				sb.append(" ");

			res.add(sb.toString());

		}


		return res;

	}
}