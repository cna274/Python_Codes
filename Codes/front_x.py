# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 18:45:33 2016

@author: Srinivas
"""

def front_x(words):
  b = []  
  c = sorted(words)
  print c
  for i in words:
      if i[0] == 'x':
          print i
          b.insert(len(b),i)
          print b
          c.remove(i)
          print c
  for j in range(len(c)):
      b.append(c[j])   
  #print b            
  #ans  = b.append(c)
  #print ans                
  return b