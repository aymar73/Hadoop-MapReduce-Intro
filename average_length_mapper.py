#!/usr/bin/python
# The key is node_id (forum_id)
# The value is length of body
# We need to ignore the comment posts
# The output is the key/node_type(question or answer)/value tuple separated by tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter="\t")

for line in reader:
    if len(line) != 19:
       # skip the line
       continue
    
    if line[5] == "question":                                          # the forum_node_id is node_id
       print "{0}\t{1}\t{2}".format(line[0], line[5], len(line[4]))
    elif line[5] == "answer":                                          # the forum_node_id is parent_id
        print "{0}\t{1}\t{2}".format(line[7], line[5], len(line[4]))
