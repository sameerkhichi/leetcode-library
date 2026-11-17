# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        if not root: return None

        def swapCurrent(curr):
            
            #Base Case
            if curr.right is None and curr.left is None:
                return

            #Three cases
            #There are both left and right children (switch them)
            #There is only right children (move it to the left)
            #There is only left children  (move it to the right)
            tempRight = curr.right
            curr.right = curr.left
            curr.left = tempRight

            #Go down one to next child
            if curr.left:
                swapCurrent(curr.left)
            if curr.right:
                swapCurrent(curr.right)
        
        #start the recursion 
        swapCurrent(root)
        
        #return root (all operations are already done to it)
        return root



        
