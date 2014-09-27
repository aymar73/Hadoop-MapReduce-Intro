#!/usr/bin/python
# Key is the author_id
# Value is the hour (from added_at field)
# We have to ignore the offset for added_at field
# The output is the key/value pair separated by tab

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter="\t", quotechar='"', quoting=csv.QUOTE_ALL)

reader.next() # to skip from the header line

for line in reader:
    if len(line) == 19:
       author_id = line[3]
       hour = line[8].split("+")
       post_hour = datetime.strptime(hour[0],'%Y-%m-%d %H:%M:%S.%f')
       post_hour = post_hour.hour
       print "{0}\t{1}".format(author_id, post_hour)
