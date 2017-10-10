// Given an absolute path for a file (Unix-style), simplify it.

// For example,
// path = "/home/", => "/home"
// path = "/a/./b/../../c/", => "/c"
// click to show corner cases.

// Corner Cases:
// Did you consider the case where path = "/../"?
// In this case, you should return "/".
// Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
// In this case, you should ignore redundant slashes and return "/home/foo".
 // 题目不清楚 eg:  /hh/home/../c/ 他要求返回的是 /hh/c
// 所以 if (tmp == ".." and !stk.empty()) stk.pop_back(); 只弹出一个而
// 不是清空之前入stk的所有string

#include<bits/stdc++.h>

using namespace std;

string simplifyPath(string path) {
    string res, tmp;
    vector<string> stk;
    stringstream ss(path);
    while(getline(ss,tmp,'/')) { //通过ss 流来分段抓string 到tmp里
	//读到 '/' 为止， ’/'直接丢弃，
		cout<<"tmp is "<<tmp<<endl;
        if (tmp == "" or tmp == ".") continue;
        if (tmp == ".." and !stk.empty()) stk.pop_back();
        else if (tmp != "..") stk.push_back(tmp);
    }
    for(int i = 0; i< stk.size(); i++) 
		res += "/"+stk[i];
    return res.empty() ? "/" : res;
}

int main(){
	string path = "/hh/home/../c/";
	cout<<simplifyPath(path);
	return 0;
}