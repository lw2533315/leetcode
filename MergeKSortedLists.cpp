// Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

#include<bits/stdc++.h>
using namespace std:

	struct ListNode {
		int val;
		ListNode *next;
		ListNode(int x) : val(x), next(NULL) {}
	};

class Solution {
public:
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		ListNode *head = new ListNode(0);
		ListNode *cur = head;

		//delete 所有空指针
		for(int i = 0 ; i< lists.size();) {
			if (lists[i] == nullptr)
				lists.erase(lists.begin() + i);
			else
				i ++;
		}

		while (lists.size() > 0) {
			int min = lists[0]->val;
			int index = 0;

			//找所有item里链表的第一个指针指向的最小值
			for(int i = 0; i< lists.size(); i++) {
				if ((lists[i]->val) < min) {
					min = lists[i]->val;
					index = i;
				}
			}

			//加入链表
			cur->next = lists[index];
			cur= cur->next;

			lists[index] = lists[index] ->next;
			if (lists[index] == nullptr)
				lists.erase(lists.begin() +index);
		}

		return head->next;


	}
};