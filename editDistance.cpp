
// Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

// You have the following 3 operations permitted on a word:

// a) Insert a character
// b) Delete a character
// c) Replace a character

// 用一个数组来存储,不同情况下字符串之间的distance，word1 长度 w1_size，
// word2 长度 w2_size,   dis数组的大小为  (w1_size+1)*(w2_size+1)
// 这是由于 要加一个初始状态dis[0][0]让这个distance为0， 即是 "" 和 ""
 
// dis[i][j] 代表长度为i和长度为j的 两个字符串之间的最小distance
// 我们知道
// dis[i][0]  words1 长为i，words2长为0，那么distance就是i
// dis[0][i]  同理distance也是i，所以先初始化这两种特殊情况

// 然后 假设i，j分别表示dis数组的row 和 col
// 那么dis[i][j],  的i是words1里面的 第i-1 个字符
				  // j是words2里面的 第j-1 个字符
// 当words1[i-1] == words2[j-] 这种情况出现时 意味着
// dis[i-1][j-1] 的情况到 dis[i][j]不用增加操作  eg  “abc"    "cdc"
// 如果i = j = 3时  words1[2] == words2[2] == 'c'
// if dis[2][2] = 2  "ab" 到”cd”  是2
// then dis[3][3] 应该 等于dis[2][2] 因为words1[2] == word2 [2]

// 如果当words1[i-1] ！= words2[j-] 就需要增加操作了 因为是DP算法所以每一个分事件都是
// 满足当前条件的最小distance， 而dis[i][j]之前可能由三种情况转化而来
// dis[i-1][j-1] ;  dis[i-1][j]; dis[i][j-1] 每一种情况的dis都表示最小distance，而从
// 这三种情况到dis[i][j]的情况都只需要进行一次操作，当考虑到长度为i，和j时
// 用replace就可以了，那么就是在以上3种情况下分别+1取最小值，也可以先去他们的最小值
// 再+ 1

 
class Solution {
public:
   
 int minDistance(string word1, string word2) {
         int w1_size = word1.length();
        int w2_size = word2.length();
        
        
       
        
        int dis[w1_size+1][w2_size+1];
        
     
        //dis[0][0] = 0 是起始状态代表 假设两个都为空时的distance为0
        for (int i = 0; i <= w1_size ; i++)
            dis[i][0] = i;
        for (int i = 0; i <= w2_size; i++)
            dis[0][i] = i;
        
        for(int i = 1; i <= w1_size; i++){
            for(int j = 1; j <= w2_size; j++){
                //当前字符相同，dis的i对应的是word里的i-1,应为dis里填充了一个dis[0][0]进去
                if (word1[i-1] == word2[j-1]){
                    dis[i][j] = dis[i-1][j-1];
                }
                else{
                    dis[i][j] = 1 + min(dis[i-1][j-1], min(dis[i][j-1], dis[i-1][j]));
                }
            }
        }
        return dis[w1_size][w2_size];
    }
};