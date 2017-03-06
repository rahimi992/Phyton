# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:39:40 2017

@author: Amin
"""
#recursion function

def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

#Fibonacci Sequence
#0,1,1,2,3,5,8,13,21,34...

print get_fib(5)
print get_fib(6)
print get_fib(7)

# dynamic memories
def get_fib(position, memo):
    if position == 0 or position == 1:
        return position
    elif not memo[position]:
        memo[position] = get_fib(position - 1, memo) + get_fib(position - 2, memo)
    return memo[position]
    

#Fibonacci Sequence
#0,1,1,2,3,5,8,13,21,34...
from collections import defaultdict

dic = defaultdict(int)

print get_fib(5, dic)
print get_fib(6, dic)
print get_fib(7, dic)

"""
function getFib(position) {
  if (position == 0) { return 0; }
  if (position == 1) { return 1; }
  var first = 0,
      second = 1,
      next = first + second;
  for (var i = 2; i < position; i++) {
    first = second;
    second = next;
    next = first + second;
  }
  return next;
}
  """