#!/usr/bin/python

import sys

student_list = []
oldid = None

# key = forum id
# value = studen id (author_id)

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
       continue

    thisid, this_author = data

    if oldid and oldid != thisid:
       student_list.sort()
       print "{0}\t{1}".format(oldid, student_list)
       oldid = thisid;
       student_list = []

    oldid = thisid
    
    # Add the student to the list of forum students
    student_list.append(this_author)

if oldid != None:
   print "{0}\t{1}".format(oldid,student_list)


