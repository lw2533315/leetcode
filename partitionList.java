Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

// 不改变原来顺序  比如2在1后面那么运行后2还在1后面，否则在1 前面
// 注意引用都是地址，没有到马上需要用的时候不要申明，避免出现非主动被修改



class Solution{
  public ListNode partition(ListNode head, int x){
    ListNode ft = new ListNode(0);
    if(head == null || head.next == null)
      return head;
    ft.next = head;
    head = ft;
    ListNode check = head;
    
    while(check.next!=null && check.next.val < x){
      check = check.next;
    }
    ft = check;
    ListNode cur = ft;
    // check.next.val >= x
    while(check.next!= null){
      
      if(check.next.val < x){
                
        // insert after temp
        ListNode temp = check.next;
        check.next = check.next.next;
        temp.next = cur.next;
        cur.next = temp;
        cur = cur.next;
        
        continue;
      }
      check = check.next;
    }
    return head.next;
  }
}