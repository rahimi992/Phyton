# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 09:28:06 2017

@author: Amin
"""

"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring of s. 
For example: if s = "udacity" and t = "ad", then the function returns True. 
"""
def question1(s, t) :
    ls = list(st)         #convert the string to the liasts
    lt = list(t)
    loc = []
    for cha in lt:       
        if cha in ls:
            loc.append(ls.index(cha))
            ls.remove(cha)
    if len(lt)==len(loc):
        mini = min(loc)   
        for i in range(0,len(loc)):
           loc[i] -= mini
    if max(loc)+1==len(loc):
        return True
    else:
        return False
        
st = "udacity"
print question1(st,"ad")     #True
print question1(st,"uy")    #False
print question1(st,"buy")   #False

"""
Question 2
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.
"""
def question2(a):
    ll = len(a)-1
    pal = []
    ss = ""
    for i in range(1,len(a)-1): # loop over characters in the string
        sub = [a[i]]
        j = 1
        while (a[i-j] == a[i+j]): # check left and rigth of a character 
            sub.append(a[i+j])
            j += 1
            if (i+j>ll or i-j<0):
                break
        if len(sub)>1:
            pal.append(ss.join(sub))
    
    index = 0
    for i in range(1,len(pal)):
        if len(pal[index]) < len(pal[i]) :
            index = i
    
    ss = ""
    for i in range(len(pal[index])-1,0,-1):
        ss += pal[index][i]
    ss += pal[index]
        
    return ss
            
aa = "abaqedede"
print question2(aa)

aa =  "abracadabra"
print question2(aa)

aa =  "bananas"
print question2(aa)

"""
Question 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. Your function should take in and return an adjacency list structured 
like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)
"""
def check_graph(g_in):  
    def connected(gg, root, path=[]): #recursive def to check if the graph is connected
        for leavs in gg[root]:
            if leavs not in path:
                path.append(leavs)
                connected(gg, leavs, path)
        return len(path) == len(gg.keys())
    
    conn = {}
    for key in g_in.keys():       #convert input dic to dic without Weights 
        conn[key] = map(lambda x: x[0], g_in[key])
            
    return connected(conn,'A', ['A'])

def question3(graph):
    edges = []
    for key in graph.keys():
        for item in graph[key]:
            node, weight = item
            # built the edges list consist of two nodes connected by a edge and weight
            if ((key, node, weight) not in edges) and ((node, key, weight) not in edges):
                edges.append((key, node, weight))
    edges = sorted(edges, key=lambda x: x[2], reverse=True) #sort the edge list

    for node1,node2,weight in edges:
        graph[node1].remove((node2, weight))  #remove the edge with largest weight
        graph[node2].remove((node1, weight))
        if check_graph(graph) == False:      #check if the graph is connected
            graph[node1].append((node2, weight)) 
            graph[node2].append((node1, weight))
    
    return graph
    
graph1 = {'A': [('B', 4), ('C', 2), ('E', 3)],
         'B': [('A', 4), ('D', 5)], 
         'C': [('A', 2), ('D',1), ('E',6), ('F',3)],
         'D': [('B',5),('C',1),('F',6)],
         'E': [('A',3),('C',6),('F',2)],
         'F': [('C',3),('D',6),('E',2)]}
print question3(graph1)

graph2 = {'A': [('B', 4), ('F', 6), ('D', 1)],
          'B': [('A', 4), ('C', 5), ('E', 2)], 
          'C': [('B', 5), ('D', 6)],
          'D': [('C', 6), ('E', 4), ('A', 1)],
          'E': [('F', 5), ('D', 4), ('B', 2)],
          'F': [('E', 5), ('A', 6)]}
print question3(graph2)

graph3 = {'A': [('B', 4), ('C', 2)],
         'B': [('A', 4), ('D', 5)], 
         'C': [('A', 2), ('D',1), ('F',3)],
         'D': [('B',5),('C',1),('F',6)],
         'E': [('F',2)],
         'F': [('C',3),('D',6),('E',2)]}
print question3(graph3)

"""
Question 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor of both nodes.
"""
def tree_path(arr, root, leaves, path=[]): #find the path from root to a given leaves
    if arr[root][leaves]==0:
        for i in range(0,len(arr[root])):
            if arr[root][i]!=0 :
                if leaves not in path:
                    path.append(i)
                    tree_path(arr, i, leaves, path)
    else:
        path.append(leaves)
    return path

def question4(T, r, n1, n2):
    path1 = tree_path(T,r,n1,[])
    path2 = tree_path(T,r,n2,[])
    return len(path1)+len(path2)

# assume each node has max two branches and 
# the left child has value less than parents while
# the right child has value greater than parents
                
def question4(T, r, n1, n2):
    counter = 0
    for nn in [n1, n2]:
        parent = r
        while parent != nn:               #left
            childs = []
            for i, child in enumerate(T[parent]):
                if child != 0 :
                    childs.append(i)
            if len(childs)>1 :
                if nn<parent :
                    parent = childs[0]
                elif nn>parent :
                    parent = childs[1]
            else:
                parent = childs[0]
            counter += 1
    return counter
# New version based on the matrix         
def question4(T, r, n1, n2):
    counter = 0
    for nn in [n1, n2]:
        row = r
        while row!=nn :
            if nn>row :
                indx = 1
            elif nn<row:
                indx = -1
            row_new = row    #row_new is actually a column 
            while T[row][row_new] == 0 :
                row_new += indx
            row = row_new
            counter += 1
    return counter

aa = [[0, 0, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0]]
print question4(aa,3,0,4)   
print question4(aa,3,1,4)
print question4(aa,3,0,5)
print question4(aa,3,2,5)
"""
Question 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
"""
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def length(self): 
        counter = 0
        current = self.head
        while current:
            current = current.next
            counter += 1
        return counter
    
def question5(ll, m):
    l = ll.length()
    pos = l-m+1
    return ll.get_position(pos).data

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.append(e5)

print question5(ll,3)
print question5(ll,5)
print question5(ll,1)
