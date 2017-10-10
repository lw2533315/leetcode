// Given a collection of distinct numbers, return all possible permutations.

// For example,
// [1,2,3] have the following permutations:
// [
  // [1,2,3],
  // [1,3,2],
  // [2,1,3],
  // [2,3,1],
  // [3,1,2],
  // [3,2,1]
// ]
//用前面做过的寻找下一个排列数的方法，知道找到自己
//从后面看起一旦发现下一个index的数比当前index数小，那么下一个index就是需要调整的起始点
// 0 1 3 2      当探测到3的时候发现下一个数是1比当前小，那么1就是起始替换点  0213

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int> > res;
        res.push_back(nums);
        if (nums.size() == 0 || nums.size() == 1)
            return res;
        vector<int> next;
        int times = 1;

        for(int i = 1; i<=nums.size(); i++)
            times*=i;

        next = getNext(nums);
        for(int i = 0; i<next.size();i++)


        while(times > 1){
            res.push_back(next);
            next = getNext(next);

            times -= 1;
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