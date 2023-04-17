#sets are evalues that are unordered and also have no duplicate

cs_course = {'math', 'chemistry', 'computer', 'physics'}
print(cs_course)
#outcome has different order of list which we have entered. it is because the order doesnt matter to cs_s
#and cs_s are generally used to remove duplicates and find wether the item is present in list or not

cs_course = {'math', 'math', 'chemistry', 'computer', 'physics'}
print(cs_course)

#to find presence of item
print('math' in cs_course)

#to find intersection 
cs_course = {'math', 'chemistry', 'computer', 'physics'}
art_course = {'art', 'chemistry', 'design', 'physics'}
print(cs_course.intersection(art_course))

#to find difference
cs_course = {'math', 'chemistry', 'computer', 'physics'}
art_course = {'art', 'chemistry', 'design', 'physics'}
print(cs_course.difference(art_course))

#to find union
cs_course = {'math', 'chemistry', 'computer', 'physics'}
art_course = {'art', 'chemistry', 'design', 'physics'}
print(cs_course.union(art_course))
 
#empty list
list1 =[]
list1 = list()

#empty tuple
tuple1 = ()
tuple1 = tuple()

#empty sets
set1 = {}#this isn't right! it's a dictionary
set1 = set()

