# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:32:21 2017

@author: Amin
"""

# read input
def read():
    s = raw_input()
    return s

#read array form input in one line
arr = map(int,raw_input().strip().split(' '))
    
from __future__ import division
# floating point division
print 4 / 3
# integer division  
print 4 // 3

#function
def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print is_leap(input())

#print function
from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i, sep='', end='')