from collections import defaultdict


diction = defaultdict(int)

print(diction)

diction['Joe']=5
print(diction)

name = 'Coop'

diction[name] = 1
print(diction)

list1 = ['Joe','Coop','Tim']
print(list1[2])

diction[list1[2]] +=1

print(diction)

subtotal = 0
for name in diction:
    subtotal += diction[name]
print(subtotal)
