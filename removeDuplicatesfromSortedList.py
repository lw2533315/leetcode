
# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
# 记住这是链表，移动指针

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return head
        val = head
        temp = head.next
        while temp != None:
            if temp.val == val.val:
                val.next = temp.next
            else:
                val = temp
            temp = temp.next
        return head
            
            