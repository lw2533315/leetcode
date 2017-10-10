
# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.





class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur = head

        if head == None: #head 是空的
            return None

        if head.next:      #判断是否长度为1，移动头指针
            head = head.next
        else:
            return head

        while cur.next:  #长度大于等于2
            temp = cur.next
            if temp.next:  #长度>=3
                if temp.next.next: #长度>=4
                    cur.next = temp.next.next
                else:
                    cur.next = temp.next
                temp1 = cur
                cur = temp.next
                temp.next = temp1

            else:
                temp.next = cur;
                cur.next = None
        return head

