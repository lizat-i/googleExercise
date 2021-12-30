#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

def mimic_dict(filename):
  if isinstance(filename, list):
    unique_list = filename
    not_unique_list = filename
  else:
    f = open(filename,"rU")
    text = f.read(),
    unique_list 		= list(set(text[0].lower().split()))   
    not_unique_list 	= text[0].lower().split() 
    
    
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++

 
  dictOfWords = {}
  dictOfWords[''] = [not_unique_list[0]]
 
  for word in unique_list:
    indices =[i for i, x in enumerate(not_unique_list) if x==word and (i+1)<len(not_unique_list)]
    words   =[not_unique_list[i+1] for i in indices]
    dictOfWords[word] = words
  return dictOfWords


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
# for word in mimic_dict : print word, mimic_dict[word]      
# +++your code here+++
#  print mimic_dict.values()
  i = 1
  text = []
  while i<10000:
    if mimic_dict[word]:
       word =  random.choice(mimic_dict[word])
       i += 1
    else:
       word ='' 
    text.append(word)  
  
  return text


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  text = print_mimic(dict, '')
  i = 1
  while i<10:
    dict = mimic_dict(text)
    text = print_mimic(dict, '')
    i +=1
  print(text[:50])
  textfile = open("output.txt","w")
  for words in text : textfile.write(words + " ")
  textfile.close()
  


if __name__ == '__main__':
  main()
