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