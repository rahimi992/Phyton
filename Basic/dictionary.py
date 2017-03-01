# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:28:20 2017

@author: Amin
"""

#dictionary
a_dict = {'one': 1} # Here 'one' is the key.
a_dict['two'] = 2 # Adds key 'two' which points to 2
print a_dict['one']
# prints 1  
if 'three' in a_dict:
    # To check whether a certain string exist as a key in the dictionary  
    print a_dict['three']
else:  
    print "Three not there"
# prints Three not there
del a_dict['one']
# Deletes index 'one' and the value associated with it  
print a_dict
# prints {'two': 2}

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)      #changed to float from int
        student_marks[name] = scores
    query_name = raw_input()

a = student_marks[query_name]
print '%.2f' %(sum(a)/len(a))

locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

print 1
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print city

print 2
asia_cities = []
for countries, cities in locations['Asia'].iteritems():
    city_country = cities[0] + " - " + countries 
    asia_cities.append(city_country)
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print city