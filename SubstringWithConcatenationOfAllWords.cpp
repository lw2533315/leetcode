// You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

// For example, given:
// s: "barfoothefoobarman"
// words: ["foo", "bar"]    长度相同，每一个只出现1次，但是可以有重复项["aa","aa"]

// You should return the indices: [0,9].
// (order does not matter).




#include<bits/stdc++.h>
#include<tr1/unordered_map>

using namespace std;
using namespace std::tr1;


class Solution {
public:
	vector<int> findSubstring(string s, vector<string>& words) {
		vector<int> res;
		if (s.empty() || words.empty()) return res;
		int n = words.size(), m = words[0].size();
		cout<<"n is "<<n<<" : "<<"m is "<<m<<endl;
		unordered_map<string, int> m1;
		//将words中的string都放入m1中作为key，值是1
		for (int i = 0; i< words.size(); i++) {
			cout<<m1[words[i]]<<" : ";
			++m1[words[i]];  //将新的item插入m1，值是0+1 = 1
			cout<<m1[words[i]]<<endl;
		}
		
		for (int i = 0; i <= s.size() - n * m; ++i) {
			unordered_map<string,int> m2;
			int j = 0;
			for (j = 0; j < n; ++j) {
				string t = s.substr(i + j * m, m);
				
				//t不在m1中跳出
				if (m1.find(t) == m1.end()) break;  
				++m2[t];
				
				//当words中的item 出现的次数多过实际应该出现的次数
				//这时跳出j不会加最后一个1，就会小于n不满足条件
				if (m2[t] > m1[t]) break;
			}
			if (j == n) res.push_back(i);
		}
		return res;
	}
};


int main() {
	string s= "barfoothefoobarman";
	vector<string> v;
	v.push_back("foo");
	v.push_back("bar");
	Solution solu;
	vector<int> res(solu.findSubstring(s,v));
	cout<<endl;
	for(int i  =0 ; i<res.size(); i++)
		cout<<res[i]<<" ";
	return 0;
}