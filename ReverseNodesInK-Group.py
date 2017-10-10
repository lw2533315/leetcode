class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None:
            return None


        pointers = []   #用来存k个指针，分别指向0->k-1个节点
        for i in range(k):
            p = head
            pointers.append(p)



        cur = head  #遍历链表的指针

        rear = head

        temp = ListNode(0)

        temp.next = head
        head = temp


        index = 0

        while(cur):

            #给points链表里指针赋值
            if (index < k):
                pointers[index % k] = cur
                cur = cur.next

                #只有当链表满了才操作，不然66行返回的是原始链表
                if index == k-1:

                    temp.next = pointers[k-1]

                    if pointers[k-1].next:  #记录一组pointers满了后之后链接的node
                        rear = pointers[k-1].next
                    else:
                        rear = None
                    temp = temp.next
                    i = k-2
                    while i >= 0:  #把在points里指向的node重新组装
                        temp.next = pointers[i]
                        temp = temp.next
                        i -= 1
                    index = -1  #因为while外有个index++所以为了让index = 0，这里要= -1
                    temp.next = rear

            index += 1



        return head.next