#!/usr/bin/python

import sys

tag_counts = 0
top_10 = []
oldtag = None

# definition of a procedure 
# returning the first element of a list: It will be called
# inside the main "for line loop"

def first_element (my_list):
    return my_list[1]

# Loop around the data
# It will be in the format key\tval
# Where key is the list of tagnames, val is the count=1
#
# All the count for a particular list of tagnames will be presented,
# then the key will change and we'll be dealing with the next list

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
       continue

    thistag, thiscount = data

    if oldtag != thistag and oldtag != None:
       top_10.append([oldtag,tag_counts])
       oldldtag = thistag;
       tag_counts = 0

    oldtag = thistag
    tag_counts += float(thiscount)

top_10 = sorted(top_10, key = first_element, reverse = True) # sorting elements in top_10 in reverse order

for tag in top_10[0:10]:  # select the first ten elements 
    print "{0}\t{1}".format(tag[0], tag[1])
