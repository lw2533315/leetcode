#include<bits/stdc++.h>

using namespace std;

int main() {
	int number;
	cin>>number;

	map<string, vector<int> >m;
	
	string result = "";
	for(int i = 0; i < number; i++) {
		vector<int> v;
		string key;
		int size;
		cin>>key;
		cin>>size;
		v.push_back(size);  //size put the first item of vector
		for (int j = 0; j < size; j++) {
			int temp;
			cin>>temp;
			v.push_back(temp);
		}
		m.insert(make_pair(key, v));
	}

	map<string, vector<int> >::iterator itr;
	itr = m.begin();
	cout<<"the size of map is "<<m.size()<<endl;

	//traverse map
	for(; itr !=m.end(); itr++) {
		//finde the key's length
		string temp = itr->first;
		int key_len = temp.length();
		char origin_value = temp[0];
		vector<int> vTemp = itr->second;
		cout<<"value's vector's size is "<<vTemp.size()<<endl;
		int pos = vTemp[vTemp[0]];  //the last item's value
		int size = key_len + pos - 1;  //pos is index+1
		cout<<"~~~the size is "<<size<<endl;

		if (result == "") {


			for (int i = 0; i < size; i ++) {
				result += origin_value;
			}
		} else {
			if (size > result.length()){
				cout<<"enlarge the result here"<<endl;
				for (int k = result.length(); k < size; k++){
					result += origin_value;
				}
				cout<<"~~~result is "<<result<<endl;
				
			}
		}

		//put each key to the corresponding position
		cout<<"before assign the key "<<result<<endl;
		for (int i = 1; i <= vTemp[0]; i++) {
			cout<<"the "<<vTemp[i]-1<<" position"<<endl;
			int index = vTemp[i] - 1;
			for(int j = 0; j < key_len; j++) {
				cout<<"string's charcter "<<temp[j]<<endl;
				
				result[index] = temp[j];
				index++;
				cout<<result<<endl;
			}
		}

	}
	
	cout<<result<<endl;

	return 0;
}