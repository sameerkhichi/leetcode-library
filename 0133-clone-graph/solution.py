"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque 

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        #use a dictionary to remember what nodes you have already cloned
        #use BFS to traverse through the graph - using loops and a FIFO queue.

        #empty node case
        if not node:
            return

        #a dictionary of cloned nodes
        cloned_nodes = {node: Node(node.val)}

        #initialize a queue using the collections import in python to proceed with bfs
        bfs_queue = deque([node])

        #while we still have items in the bfs queue (neighbors we havent visited)
        while bfs_queue:
            
            #get the current node (FIFO)
            current_node = bfs_queue.popleft()

            #for each neighbor of the current nodes
            for neighbor in current_node.neighbors:
                #check if we have already cloned the neighbor
                if neighbor not in cloned_nodes:
                    cloned_nodes[neighbor] = Node(neighbor.val) #if we havent clone it
                    bfs_queue.append(neighbor) #append the neighbor into the queue so we can process ITS neighbors later (thats how bfs works)

                #Get the newly cloned current node
                #.neighbors opens up the empty list of neighbors on that newly cloned node
                # Then add the CLONED neigbors references to the list of neighbors of said newly cloned node.
                cloned_nodes[current_node].neighbors.append(cloned_nodes[neighbor])

        return cloned_nodes[node]




