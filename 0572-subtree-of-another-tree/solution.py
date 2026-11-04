from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        
        #Use a BFS technique to itterate through the tree.
        #at each node check weather the current node is equal to subRoot
        #if it is return true
        #if it makes it to the end of the tree without finding one then return false
        
        #initialize the queue for a breadth first search
        queue = deque()
        queue.append(root)

        #at each node check if the current node and its children are the same as the subRoot
        #this will be a recursive function as it has to make sure everything in the two trees are the same
        #the moment something isnt the same - break and return false
        def isSame(curr, subRoot):
            mainQueue = deque()
            mainQueue.append(curr)
            subQueue = deque()
            subQueue.append(subRoot)

            #go through the current nodes subtree and compare it with the given subtree
            while mainQueue and subQueue:
                main = mainQueue.popleft()
                sub = subQueue.popleft()
                
                if not main and not sub: #the structure matches so far
                    continue

                #at any point they dont match this subtree isnt the same as the subtree given - order of this condition is important
                if (not main or not sub) or main.val != sub.val: #also checking if one of the two are none 
                    return False
                
                #queuing everything including none values to handle asymetric children in subtrees.
                mainQueue.append(main.left)
                subQueue.append(sub.left)
                mainQueue.append(main.right)
                subQueue.append(sub.right)
            
            #if one of the ques are empty while the other isnt, then that means they are not a match since the subtree continues and out given doesnt
            if mainQueue and not subQueue:
                return False
            if subQueue and not mainQueue:
                return False
            else:
                return True #if it made it all the way here that means this IS a subtree that matches the given subTree

        while queue:
            curr = queue.popleft() #get the root from the queue

            if isSame(curr, subRoot):
                return True
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return False
