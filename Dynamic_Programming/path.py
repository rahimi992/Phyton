# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 22:02:47 2017

@author: Amin
"""
"""Count the number of path"""

def path(grid, row, col, mem):
    dim = len(grid)
    position = col*dim + row
    print row, col, mem[position]
    if row == dim-1 and col == dim-1:
        return 1
    
    if mem[position] == 0 :
        if row+1 < dim :
            print position, mem[position]
            mem[position] += path(grid, row+1, col, mem)
            print position, mem[position]
        
    
        if col+1 < dim :
            print position, mem[position]
            mem[position] += path(grid, row, col+1, mem)
            print position, mem[position]

    return mem[position]

a = [[0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],]

from collections import defaultdict
dic = defaultdict(int)

path(a, 2, 2, dic)
#########################################################
def shortPath(grid, row, col, mem, result, path):
    dim = len(grid)
    position = row*dim + col
#    print row, col, mem[position]
    if row == dim-1 and col == dim-1:
        print result
        for ii in range(len(result)):
            path[result[ii]].append(result[ii:])
        print path
        return 1
    
    if mem[position] == 0 :
        if row+1 < dim and grid[row+1][col] == 0:
            if position not in result:
                result.append(position)
            mem[position] += shortPath(grid, row+1, col, mem, result, path)  
        
        if col+1 < dim and grid[row][col+1] == 0:
            if position not in result:
                result.append(position)
            mem[position] += shortPath(grid, row, col+1, mem, result, path)
    else:
        for ii, value in enumerate(result):
            for pp in path[position]:
                print result[ii:] + pp
                path[value].append(result[ii:] + pp)
        print path
        

    print position
    if len(result) != 0 :
        result.pop()
    return mem[position]

a = [[0, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 1, 0, 0, 0],]

from collections import defaultdict
dic = defaultdict(int)
path = defaultdict(list)
ss = []
shortPath(a, 0, 0, dic, ss, path)

for ii, val in enumerate(path[0]):
    print ii, len(val)

