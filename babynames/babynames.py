#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def get_file_as_list_of_words(filename):
    f = open(filename, "rU")
    text = f.read()
    return text


def find_helper(pat, tex, groupswitch=0):
    match = re.search(r'%s' % pat, tex)
    if match:
        print(match.group(groupswitch))
    else:
        print('notFound!')


def extract_names(filename):
    """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
    teststring = get_file_as_list_of_words(filename='baby1990.html')
    year  = re.search('Popularity in (\d\d\d\d)</h3>',teststring)
    print year.groups(1)
    match = re.findall('tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', teststring)
    dict_name_rank = {}
    for rank_gend_tuple in match:
        # TODO: add HERE AFTERWARDS TWO CHECK WRAPPERS IF THER entries are already given
        # TODO: adnd if the ranke is higher ow lower then the list which is inside
        dict_name_rank[rank_gend_tuple[1]] = rank_gend_tuple[0]
        dict_name_rank[rank_gend_tuple[2]] = rank_gend_tuple[0]
    year_names_and_ranks_sorted = sorted(dict_name_rank.items())
  
    return year_names_and_ranks_sorted


# . (dot) any char
# \w word char
# \d digit
# \s whitespace
# \S non-whitespace
# + 1 or more
# 0 or more
def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    print args[0]
    rny_list = extract_names(args[0])

if __name__ == '__main__':
    main()
