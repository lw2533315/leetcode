// Given a list, rotate the list to the right by k places, where k is non-negative.

// For example:
// Given 1->2->3->4->5->NULL and k = 2,
// return 4->5->1->2->3->NULL.



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next)
            return head;
        
        ListNode* worker = head;
		
		//找到链表长度
        int count = 0;
        while(worker){
            worker = worker->next;
            count += 1;
        }
		
		//简化移动的距离
        k = k % count;
        if (k == 0)
            return head;
			
		//寻找需要打断的指针所属的节点
        worker = head;
        while(count >  k + 1){
            worker = worker->next;
            count -= 1;
        }
     
		//移动到链表最后为链接head做准备
        ListNode* temp = worker;
        while(worker->next){
            worker = worker->next;
        }
        
		//处理两个链接点，一个断点
        worker->next = head;
        head = temp->next;
        temp->next = nullptr;
       
        return head;
        
    }
    
    
};