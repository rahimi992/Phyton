# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 21:58:34 2017

@author: Amin
"""

from itertools import product
a,b = [map(int,raw_input().split()) for _ in range(2)]
print " ".join(map(str, list(product(a,b))))

from itertools import permutations
print list(permutations(['1','2','3','4'],2))  

from itertools import permutations
inputs = raw_input().split()
print "\n".join( "".join(i) for i in permutations(sorted(inputs[0]),int(inputs[1])) ) 


from itertools import combinations
print list(combinations('12345',2))

S, K = raw_input().split()
for k in range(1,int(K)+1):
    print "\n".join("".join(i) for i in list(combinations(sorted(S),k)))
    

from itertools import combinations_with_replacement
print list(combinations_with_replacement('1234',2))

from itertools import groupby
print " ".join(str((len(list(k)),int(i))) for i,k in groupby(raw_input()))

########################
import itertools
N = int(raw_input())
string = raw_input()
K = int(raw_input())

a_occurences = ['a' in ["".join(string.split(" "))[i] for i in tu] for tu in itertools.combinations(range(N), K)]
print float(sum(a_occurences)) / len(a_occurences)
#4 
#a a c d
#2
###############################

from itertools import product
K,M=[int(x) for x in raw_input().split()]
print max([sum([y*y for y in x]) % M for x in product(*[[int(y) for y in raw_input().split()[1:]] for i in range(K)])])

#3 1000
#2 5 4
#3 7 8 9 
#5 5 7 8 9 10 