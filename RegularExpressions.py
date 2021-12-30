#!/usr/bin/env python

# . (dot) any char
# \w word char
# \d digit
# \s whitespace
# \S non-whitespace
# + 1 or more
# 0 or more

import sys
import re
# Define HelperFunction

def Find(pat, tex, groupswitch=0):
  match = re.search(r'%s'%pat,tex)
  if match:  print match.group(groupswitch)
  else:  print 'notFound!'


# Define a main()
def main():
  textExample = 'sadjk .s.fsda@sdflksdafmlkasdfsdafs ivan.lizat@outlook.de iweaufdni efwu dfsdfsdfsd.sdfsdfsdfsdfsdf'
  Find('\s\w+\.\w+\@\w+\.\w+',textExample)
  Find('\s\w+\.\w+\@\w+\.\w+',textExample,0)
  Find('(\s\w+\.\w+)\@(\w+\.\w+)',textExample,1)
  Find('(\s\w+\.\w+)\@(\w+\.\w+)',textExample,2)
  
  match = re.findall('\s\w+\.\w+\@\w+\.\w+',textExample)  
  print match
  
  return None

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

