# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:25:16 2017

@author: Amin
"""

#List
arr = list()
# or simply
arr = []; arr = [1,2,3]

print arr[0] # result is 1
print arr[0] + arr[1] + arr[2] # result is 6

arr.append(9)   
print arr  # prints [1, 2, 3, 9]

arr.extend([10,11])
print arr # prints [1, 2, 3, 9, 10, 11]

arr.insert(3,7) #insert 7 at position 3
print arr # prints [1, 2, 3, 7, 9, 10, 11]

arr.remove(10)  
arr  # prints [1, 2, 3, 7, 9, 11]

temp = arr.pop() #remove the last element
print temp  # prints 11

temp = arr.index(3) #Returns the first index of a value in the list
print temp # prints 2

temp = arr.count(1) #Counts the number of occurrences of an element x.
print temp # prints 1

arr.sort()
print arr # [1, 2, 3, 7, 9]

arr.reverse()
print arr # [9, 7, 3, 2, 1]

# create sub list
sub = [x for x in arr if x not in [3,7]]

# list question
if __name__ == '__main__':
    n = input()
    l = []
    for _ in range(n):
        s = raw_input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print l
## input 
#12
#insert 0 5
#insert 1 10
#insert 0 6
#print 
#remove 6
#append 9
#append 1
#sort 
#print
#pop
#reverse
#print
## output
#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]

#Tuples are data structures that look a lot like lists. Unlike lists, tuples are immutable 
#(meaning that they cannot be modified once created). This restricts their use because 
#we cannot add, remove, or assign values; however, it gives us an advantage in space 
#and time complexities.

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    integer_tuple = tuple(integer_list)
    print hash(integer_tuple)

# List Comprehensions
a, b, c, n = [int(raw_input()) for _ in xrange(4)]
print [[x,y,z] for x in xrange(a + 1) 
               for y in xrange(b + 1) 
               for z in xrange(c + 1) 
               if x + y + z != n]

#Nested list; find the second min
a = [[raw_input(), float(raw_input())] for i in xrange(int(raw_input()))]
s = sorted(set([x[1] for x in a]))
print s
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print name
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39