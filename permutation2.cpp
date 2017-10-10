// Given a collection of numbers that might contain duplicates, return all possible unique permutations.

// For example,
// [1,1,2] have the following unique permutations:
// [
  // [1,1,2],
  // [1,2,1],
  // [2,1,1]
// ]

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
          vector<vector<int> > res;
        res.push_back(nums);
        if (nums.size() == 0 || nums.size() == 1)
            return res;
        vector<int> next;



        next = getNext(nums);
        for(int i = 0; i<next.size();i++)


        while(nums != next){    //通过 ==  !=判断两个vector是否完全一致
            res.push_back(next);
            next = getNext(next);


        }

        return res;
    }


    vector<int> getNext(vector<int>v){
        int point = -1;
        vector<int>temp;
        for(int i = v.size() -1; i>0 ; i-- ){
            temp.push_back(v[i]);
            if (v[i-1] <v[i]){      //找到起始替换点
                cout<<"test 0: i is "<<i<<endl;
                point = i -1;
                break;
            }
        }


        //find the v is descent order   起始替换点不存在证明当前vector是从大到小排列
		//需要改成从小到大排序
        if (point == -1){
            sort(v.begin(), v.end());
            return v;
        }

        sort(temp.begin(),temp.end()); //到当前点为止所有的遍历过的term排序，
        for(int i = 0; i< temp.size(); i++)  //找到第一个大于index -1 为止元素的term 交换
            if (temp[i] > v[point]){
                swap(v[point], temp[i]);
                break;
            }

        //讲剩余的元素排序替换掉v里对应的term
        sort(temp.begin(),temp.end());

        int temp_index = 0;

        for(int i = point+1; i<v.size(); i++){
            v[i] = temp[temp_index];
            temp_index++;
        }

        return v;
    }
};