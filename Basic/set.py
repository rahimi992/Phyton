# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 00:37:12 2017

@author: Amin
"""
#A set is an unordered collection of elements without duplicate entries. 
print set()
print set('HackerRank')
print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
print set((1,2,3,4,5,5))
print set(set(['H','a','c','k','e','r','r','a','n','k']))
print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))

# create a set
myset = {1, 2} # Directly assigning values to a set
myset = set()  # Initializing a set
myset = set(['a', 'b']) # Creating a set from a list
print myset

#MODIFYING SETS
myset.add('c')
myset.add('a') # As 'a' already exists in the set, nothing happens
myset.add((5, 4))
print myset

myset.update([1, 2, 3, 4]) # update() only works for iterable objects
print myset
myset.update({1, 7, 8})
print myset
myset.update({1, 6}, [5, 13])
print myset

#Both the discard() and remove() functions take a single value as an argument and removes 
#that value from the set. If that value is not present, discard() does nothing, 
#but remove() will raise a KeyError exception.
myset.discard(10)
print myset
myset.remove(13)
print myset

#COMMON SET OPERATIONS
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
print a.union(b) # Values which exist in a or b
print a.intersection(b) # Values which exist in a and b
print a.difference(b) # Values which exist in a but not in b
print a.symmetric_difference(b) # Values which exist in a or b but not in both

a.union(b) == b.union(a)
a.intersection(b) == b.intersection(a)
a.difference(b) == b.difference(a)

#Print symetric difference
# ^ symbol can also be used to compute the symmetric difference of two sets.
m = raw_input().split()
n = raw_input().split()

print "\n".join(sorted(list(set(m) ^ set(n)),key=int))

# if AR elements in AR1 add 1, if in AR2 add -1 to happiness
AR = map(int,raw_input().split())
AR1 = set(map(int,raw_input().split()))
AR2 = set(map(int,raw_input().split()))
inter = [ k for k in AR if k in AR1]
l1 = len(inter)
inter2 = [ k for k in AR if k in AR2]
l2 = len(inter2)
print l1-l2

#You have a non-empty set S, and you have to execute N commands given in N lines.
if __name__ == '__main__':
    n = int(input())
    s = set(map(int,raw_input().split())) 
    n = int(input())

    for i in xrange(n):
        lst = raw_input().split()
        eval('s.'+lst[0]+'('+",".join(lst[1:]) +")")
print(sum(s))

# union of two sets
#input format
#9
#1 2 3 4 5 6 7 8 9
#9
#10 1 2 3 11 21 55 6 8
a,b=[set(list(map(int,raw_input().split(" ")))) for _ in range(4)][1::2]
print(len(a.union(b)))

#Set Mutations
H = set("Hacker")
R = set("Rank")
H.update(R)
H.intersection_update(R)
H.difference_update(R)
H.symmetric_difference_update(R)

A = set(map(int, raw_input().split()))

for _ in range(int(raw_input())):
    cmd = raw_input().split()
    temp = set(map(int, raw_input().split()))
    eval("A.{0}(temp)".format(cmd[0]))
    
print sum(A)


