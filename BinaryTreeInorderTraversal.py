# Given a binary tree, return the inorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
   # 1
    # \
     # 2
    # /
   # 3
# return [1,3,2].
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
     
        cur = root
        self.recur(res, cur )
        return res
        
    def recur(self, res, cur ):
        if cur == None:
            return
        
        if cur.left != None:
            self.recur(res, cur.left)
        
        res.append(cur.val)
        
        if cur.right != None:
            self.recur(res, cur.right)