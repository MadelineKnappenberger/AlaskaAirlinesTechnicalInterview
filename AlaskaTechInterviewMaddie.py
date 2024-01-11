#Maddie Knappenberger
#Alaska Airlines Technical Interview Take Home

from collections import Counter

#initalize input list
mech=[[3, 8], [0, 5], [10, 18], [0, 3], [5, 10], [2, 6], [6, 10]]

#initalize empty lists
#lst for appending expanded range
#flattenlst for flattening result from expanding ranges
lst=[]
flattenlst=[]

#loop through every entry in mech
#for each, grab range between the two numbers 
#(inclusive on the first and exclusive on the second)
#o(n) run time
for row in mech:
    num = list(range(row[0],row[1]))
    lst.append(num)

#take result and flatten, so it can run through counter
#o(n) run time
for entry in lst:
    for inner in entry:
        flattenlst.append(inner)

#Count occurences
#Constant run time
c = Counter(flattenlst)

#print out original list with number of required mechanics 
print(mech, end = '')
print(' = ', end = '')
#use Counter's most_common function, return only the top
#from that, take only the relevant info: the number of occurrences of the most common number
print(c.most_common(1)[0][1])
