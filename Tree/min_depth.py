# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 09:47:19 2017

@author: Amin
"""
# Python program to find minimum depth of a given Binary Tree
""" O(n) as it traverses the tree only once. """ 
# Tree node
class Node:
    def __init__(self , key):
        self.data = key 
        self.left = None
        self.right = None
 
def minDepth(root):
    # Corner Case.Should never be hit unless the code is 
    # called on root = NULL
    if root is None:
        return 0
     
    # Base Case : Leaf node.This acoounts for height = 1
    if root.left is None and root.right is None:
        return 1
     
    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return minDepth(root.right)+1
     
    # If right subtree is Null , recur for left subtree
    if root.right is None:
        return minDepth(root.left) +1
     
    return min(minDepth(root.left), minDepth(root.right))+1
 
# Driver Program 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print minDepth(root)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 


# Python program to find minimum depth of a given Binary Tree
 """ Faster """
# A Binary Tree node
class Node:
    # Utility to create new node
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None
 
def minDepth(root):
    # Corner Case
    if root is None:
         return 0
 
    # Create an empty queue for level order traversal
    q = []
     
    # Enqueue root and initialize depth as 1
    q.append({'node': root , 'depth' : 1})
 
    # Do level order traversal
    while(len(q)>0):
        # Remove the front queue item
        queueItem = q.pop(0)
     
        # Get details of the removed item
        node = queueItem['node']
        depth = queueItem['depth']
        # If this is the first leaf node seen so far
        # then return its depth as answer
        if node.left is None and node.right is None:    
            return depth 
         
        # If left subtree is not None, add it to queue
        if node.left is not None:
            q.append({'node' : node.left , 'depth' : depth+1})
 
        # if right subtree is not None, add it to queue
        if node.right is not None:  
            q.append({'node': node.right , 'depth' : depth+1})
 
# Driver program to test above function
# Lets construct a binary tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print minDepth(root)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)