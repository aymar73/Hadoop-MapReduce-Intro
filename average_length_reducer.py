#!/usr/bin/python

import sys

oldid = None
len_post = 0
answer_count = 0
len_answer = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the forum id and the length of body is the value
#
# All the length of body for a particular forum_id will be presented,
# then the key will change and we'll be dealing with the forum_id

def print_average_length(id, len_post, len_answer, answer_count):     # print out the results
    print "{0}\t{1}\t{2}".format(id, len_post, 0 if answer_count == 0 else float(len_answer)/answer_count)

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3:
        # Something has gone wrong. Skip this line.
       continue

    thisid, thisnode, thislen = data

    if oldid and oldid != thisid:
       print_average_length(oldid,len_post,len_answer, answer_count)
       oldid = thisid;
       len_post = 0
       len_answer = 0
       answer_count = 0
    oldid = thisid

    if thisnode == "question":
       len_post = thislen
       
    else: # an answer
       # get the sum of lengths of count and count the number to calculate the average
       len_answer += int(thislen)
       answer_count += 1

if oldid != None:
   print_average_length(oldid, len_post, len_answer, answer_count)

