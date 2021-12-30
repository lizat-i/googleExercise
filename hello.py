#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
#import json

# dir(function) and help(function)
# sorting magic sorted(a,key=len,reverse=False)
# list = a [1,2,'3',5, "absdjlfh"]
# tuple= a (1,2,'3',5, "absdjlfh")

## PrintInputfunction
def printInput(terminalInput):
  if len(terminalInput) >= 2:
    name = terminalInput[1]
  else:
    name = 'World'
  print 'Hello', name

## Sortinghelperfunction
def LastElement(x):
  return(x[-1])

def cat(filename):
  lines = open(filename, "rU").readlines()
  text = open(filename, "rU").read()

  return  text, lines

# Define a main()
def main():
   #printInput (sys.argv):
   #a = ['d','bb','aaaaz','ccc']
   #print(sorted(a,key=a[-1],reverse=False))
   #print(sorted(a,key=LastElement,reverse=True))
   #print(type(a))
   #variableA = " ".join(a)
   #print(type(variableA))
   #variableA = variableA.split(" ")
   #print(type(variableA))
   ## Dictionaries, important
   #e.g
   #hashtable = {}
   #hashtable['a'] = "alpha"
   #hashtable['o'] = "omega"
   #hashtable['g'] = "gamma"

   #text, lines = cat(sys.argv[1])

   ## Regular expressions Stuff
   match = re.search("iig","thisPiig")
   print type(match)

   return None

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()







