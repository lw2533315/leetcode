
#include<bits/stdc++.h>

using namespace std;
class Solution {
public:
   
    int minDistance(string word1, string word2) {
		 cout<<"test 0"<<endl;
         int w1_size = word1.length();
        int w2_size = word2.length();
        cout<<"test 1"<<endl;
        
        int dis[w1_size][w2_size];
        
        for (int i = 0; i < w1_size ; i++)
            dis[i][0] = i;
        cout<<"test 2 "<<endl;
        for (int i = 0; i < w2_size; i++)
            dis[0][i] = i;
        
        for(int i = 1; i < w1_size; i++){
            for(int j = 1; j < w2_size; j++){
                if (word1[i] == word2[j]){
                    dis[i][j] = dis[i-1][j-1];
                }
                else{
                    dis[i][j] = 1 + min(dis[i-1][j-1], min(dis[i][j-1], dis[i-1][j]));
                }
            }
        }
        return dis[w1_size - 1][w2_size - 2];
    }
};

int main() {
	Solution s;
	cout<<s.minDistance("aba", "efa");
	return 0;
}