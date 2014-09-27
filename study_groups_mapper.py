#!/usr/bin/python

# We want elements 0(node_type), 3(author_id), 5(node_type) and 6(parent_id)
# We need to write out to standard output node_id as a key and author_id as value if node_type is a question separated by a tab
# Or to write out parent_id as a key and author_id as value if node_type is answer or comment.

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = "\t")

for line in reader: # Looping around standard input which gives us a line at the time
 
    if len(line) == 19: # To make sure things don't break in the middle of my data

       if line[5] == "question": # the node type is a question
          print "{0}\t{1}".format(line[0],line[3])

       else: # something other than a question
          print "{0}\t{1}".format(line[6],line[3])
