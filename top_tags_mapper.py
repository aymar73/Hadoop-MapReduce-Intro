#!/usr/bin/python

# We want two elements: key = tagname , value = the count of tagname in reducer
# We need to write key/node_type tuple  out to standard output, separated by a tab

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = "\t")

for line in reader:
    if len(line) == 19:

       tag = line[2].split(" ")
       # node_type = line[5]

       if line[5] == "question":
          for i in tag:
              print "{0}\t{1}".format(i,1)

       else:
          if line[5] != "answer"or line[5] != "comment":
             continue
