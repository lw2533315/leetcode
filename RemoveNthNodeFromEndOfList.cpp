// Given a linked list, remove the nth node from the end of list and return its head.

// For example,

   // Given linked list: 1->2->3->4->5, and n = 2.

   // After removing the second node from the end, the linked list becomes 1->2->3->5.
// Note:
// Given n will always be valid.
// Try to do this in one pass.

// 用一个指针先向后移动n次，如果成功了说明从后数n个node不是head指向的node
// 如果最后一次移动不了，说明要删掉第一个指针，其他情况是n不存在
// 然后用第二个工作指针指向头node，然后同时移动这两个指针，当第一个指针
// 指向null时，第二个指针就指向了要移除的节点之前的节点



  struct ListNode {
    int val;
     ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;

		//第一个指针定位
        while(n>0){

			//如果下一个没有到null那么移动n次
            if(temp->next){
                temp = temp->next;
                n --;
                continue;
            }

			//能移动n-1次说明要删除的是第一个节点
            if(n==1){
                head = head->next;
                return head;
            }

            else
                return nullptr;
        }

		//设置第二个指针，两个指针同步移动
        ListNode* worker = head;
        while(temp->next){
            temp= temp->next;
            worker = worker->next;
        }

        worker->next = worker->next->next;
        return head;
    }
};