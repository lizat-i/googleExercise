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

def find_helper(pat, tex, groupswitch=0):
  match = re.search(r'%s'%pat,tex)
  if match:  print(match.group(groupswitch))
  else:  print('notFound!')


# Define a main()
def main():
  text_example = 'sadjk .s.fsda ivo80.17@hotmail.de @sdflksdafmlkasdfsdafs ivan.lizat@outlook.de iweaufdni efwu dfsdfsdfsd.sdfsdfsdfsdfsdf'
  find_helper('\s\w+\.\w+\@\w+\.\w+',text_example)
  find_helper('\s\w+\.\w+\@\w+\.\w+',text_example,0)
  find_helper('(\s\w+\.\w+)\@(\w+\.\w+)',text_example,1)
  find_helper('(\s\w+\.\w+)\@(\w+\.\w+)',text_example,2)

  match = re.findall('\s\w+\.\w+\@\w+\.\w+',text_example)
  print(type(match))

  return None

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

