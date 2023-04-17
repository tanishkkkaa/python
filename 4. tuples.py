#tuples are immutable and list are mutable because they can be modified

#mutable
list1 = ['history', 'maths', 'physics', 'computer']
list2 = list1
print(list1)
print(list2)
list1[0] = 'art'
print(list1)
print(list2)

#immutable
tuple1 = ('history', 'maths', 'physics', 'computer')
tuple2 = tuple1
print(tuple1)
print(tuple2)
tuple1[0] = 'art'
print(tuple1)
print(tuple2)#will show error because it is immutable(cannot be modified)
