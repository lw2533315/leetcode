# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.
#四个指针解法， pre，cur，n_1, n_2


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
        
        
        new_node = ListNode(head.val + 1)
        new_node.next = head
        head = new_node
        cur = head.next
        pre = head
        
        
        n_1 = cur.next
        n_2 = None
        if n_1 != None:
            n_2 = n_1.next
            
        
        
        
        dup_flag = False
        while n_1 != None:
            
            if dup_flag:
                
                if n_2 == None:
                   
                    if cur.val != n_1.val:
                        pre.next = n_1
                    else:
                        pre.next = None
                    
                    n_1 = None #设置跳出
                elif n_1 == n_2:
                   
                    cur = n_1
                    n_1 = n_2
                    n_2 = n_2.next
                else:
                   
                    pre.next = n_1
                    cur = n_1
                    n_1 = n_2
                    n_2 = n_2.next
                    dup_flag = False
                    
            
            elif cur.val != n_1.val:
                dup_flag = False
                pre = cur
                cur = n_1
                n_1 = n_2
                if n_2 != None:
                    n_2 = n_2.next
            
            elif cur.val == n_1.val:
                
                if n_2 != None:
                    n_1 = n_2
                    n_2 = n_2.next
                else:
                    pre.next = n_2
                    n_1 = None #跳出
                if n_1 != None and cur.val != n_1.val:
                    dup_flag = True
                
            
                
            
            
        
            
            
            
        return head.next