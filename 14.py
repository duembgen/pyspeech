#!/usr/bin/env python

''' 
what is going on here?
'''

def change_the_list(a):
    a[-1] = 'weekends.'
    print('inside:',a)

def do_not_change_the_list(a):
    b = []
    b[:len(a)] = a
    b[-1] = 'Mondays.'
    print('inside:',b)

b = ['I','hate','Mondays']
print('outside: before',b)
change_the_list(b)
print('outisde: after ',b)
