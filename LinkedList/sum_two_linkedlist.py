# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 19:33:52 2017

@author: Amin

sum two linkedlist with same size
"""

class Element(object):
    def __init__(self, value):
        self.value = value
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

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
    def add(self, linklist):
        current1 = self.head
        current2 = linklist.head
        sum_linked = LinkedList()
        
        length = 0
        while current1 and current2:
            ee = Element(current1.value + current2.value)
            sum_linked.append(ee)
            current1 = current1.next
            current2 = current2.next
            length +=1 
        
        dd = 0
        for ii in range(length):
            current = sum_linked.head
            for jj in range(length-ii):
                if jj == length-ii-1:
                    div, mod = divmod(current.value, 10)
                    print div, mod
                    if div > 0 :
                        current.value = mod + dd
                        dd = div
                    else:
                        dd = 0
                else:
                    current = current.next
               
        if dd != 0 :
            ee = Element(dd)
            sum_linked.insert(ee,1)
                               
        return sum_linked
    
e1 = Element(5)
e2 = Element(6)
e3 = Element(3)
# Start setting up a LinkedList
l1 = LinkedList(e1)
l1.append(e2)
l1.append(e3)

e1 = Element(8)
e2 = Element(4)
e3 = Element(2)
# Start setting up a LinkedList
l2 = LinkedList(e1)
l2.append(e2)
l2.append(e3)

l3 = l1.add(l2)

l3.head.value
l3.head.next.value
l3.head.next.next.value
        