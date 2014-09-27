# !usr\bin\python

oldid = None
max_hour = 0
i = 0
list_hour=array.array('i',(0,)*24)              # setting the elements of the list

# Loop around the data
# It will be in the format key\tval
# Where key is the author id, val is the index position
#
# All the positions for a particular author will be presented,
# then the key will change and we'll be dealing with the next author...


for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisid, thishour = data

    if oldid and oldid != thisid:
       max_hour = max (list_hour)               # To Store the maximum element in the list
       for i in range(0,24):                    # For every index in the list
           if list_hour[i] == max_hour:         # If the index (position) corresponds to the max element of the list
              print "{0}\t{1}".format(oldid, i) # Print out author_id and index (position)
       list_hour = array.array('i',(0,)*24)
       max_hour = 0
    oldid = thisid
    list_hour[int(thishour)] += 1               # list storing the hour counts for each author_id

if oldid != None:
   max_hour = max(list_hour)
   for i in range(0,24):
       if list_hour[i] == max_hour:
          print "{0}\t{1}".format(oldid,i)
