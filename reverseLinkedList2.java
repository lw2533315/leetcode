
// Reverse a linked list from position m to n. Do it in-place and in one-pass.

// For example:
// Given 1->2->3->4->5->NULL, m = 2 and n = 4,

// return 1->4->3->2->5->NULL.

// Note:
// Given m, n satisfy the following condition:
// 1 ≤ m ≤ n ≤ length of list.


// 在m出现之前定一个位， n结束的后面定个位，中间部分申明ListNode
// 数组存储他们的引用。然后反向遍历一遍数组(非空的item）链接之前
// 留下的两个定位

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode ft = new ListNode(0);
        if (m >= n)
            return head;
        ft.next = head;
        head = ft;
        ListNode pre_m = head;
        int index  = 1;
		
		//申明listnode数组
        ListNode [] p_arry = new ListNode[n - m + 1];
        
		//找到m之前一个节点
        while (index < m){
            pre_m = pre_m.next;
            index++;
            
        }
        
        index--; //同步index和work指针
        ListNode worker = pre_m;
        int arry_index = 0;
        
		//找到最后一个节点或者n节点，因为n可能大于链表size
        while (worker.next != null && index < n) {
            p_arry[arry_index] = worker.next;
            arry_index++;
            index++;
            worker = worker.next;
        }
        
		//找到n之后的一个 节点或者空节点
        worker = worker.next;
        
		//重新连接链表
        for (int  i = arry_index - 1; i >= 0; i--){
                pre_m.next = p_arry[i];
                pre_m = pre_m.next;
            }
            pre_m.next = worker;
        
        return head.next;
    }
}