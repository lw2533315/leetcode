#include<bits/stdc++.h>
using namespace std;

/*Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.*/


int main() {
	string str = "2147483648";
	int len = str.length();
	cout<<"size of str is "<<len<<endl;
	bool get_digit = false;
	bool t_to_f = false;
	bool get_nonDigit = false;
	bool neg = false;
	bool dup_add = false;
	bool dup_sub = false;
	bool dup_dot =false;
	bool dup_space =false;
	int ret = 0;
	vector<char>v;
	// bool number_dot = 0;
	if (len == 0 ) return  0;
	else if(len == 1 ) {     //one digit number
		if (str[0] >= 48 && str[0] <= 57)
			return str[0]-48;
		else
			return 0;
	} else {
		cout<<"test 1 ~~~~"<<endl;
		for(int i=0; i< len; i++) {

			if (get_digit == true && (str[i] == ' ' ||str[i] == '+' || str[i] == '-' || str[i] == '.' ))
				break;

			if(str[i] == '.') {
				if( dup_dot == false && dup_add == false && dup_sub==false) {
					dup_dot =true;
					break;
				} else if(dup_dot == true || dup_add == true || dup_sub==true)
					return 0;
			}
			if(str[i] == '-') {
				if( dup_dot == false && dup_add == false && dup_sub==false) {
					dup_sub = true;
					if (i+1 <len && str[i+1]>=48 && str[i+1]<=58)
						neg = true;
				} else if(dup_dot == true || dup_add == true || dup_sub==true) return 0;
			}
			cout<<"test4 ~~~~~~~"<<endl;
			if(str[i] == '+') {
				if (dup_dot == false && dup_add == false && dup_sub==false) dup_add = true;
				else if(dup_dot == true || dup_add == true || dup_sub==true) return 0;
			}
			cout<<"test3~~~~~~~~"<<endl;
			if(str[i] == ' ' ) {
				if(dup_dot == false && dup_add == false && dup_sub==false) dup_space =true;
				else if(dup_dot == true || dup_add == true || dup_sub==true) return 0;
			}
			cout<<"test2 ~~~~~~"<<endl;
			if(str[i]<48 || str[i] >57) {
				if (str[i] != ' ' && str[i] != '+' && str[i] != '-' && str[i] != '.')

					break;


			}



			if (str[i] >=48 && str[i] <=57 ) {
				cout<<"str[ "<<i<<"] is "<<str[i]<<endl;
				v.push_back(str[i]);
				get_digit = true;
			}



		}

		if(v.size() == 0)
			return 0;

	}
	cout<<"size of vector : "<<v.size()<<endl;
	int power = 0;
	for (int i = v.size()-1; i>=0; i--) {
		ret= ret + (v[i]-48)*pow(10,power);
		power ++;
	}
	cout<<"neg is "<<neg<<endl;

	if (neg)
		cout<< 0-ret;
	else
		cout<< ret;     //没有考虑越界，2^31 开始为负数



}




