#1. printing list
courses = ['history', 'maths', 'physics', 'computer']
print(courses)
#lenght of list
print(len(courses))
#2. to access individual values
print(courses[2])
print(courses[-1])
#print(courses[5])
#to grab number of values
print(courses[:2])
print(courses[1:])
#3. to add course
courses.append('electrical')#append just insert list at last
print(courses)
#to add course at specific location
#courses.insert(2, 'electrical')#it insert another list within a list not individual items within a list 
#print(courses)
courses2 = ['electrical', 'electronics']
#courses.insert(0, courses2)
#print(courses)
#print(courses[0])#output coming with this is not what we wanted so we will use another argument
courses.extend(courses2)#it insert individual items of list to list
print(courses)
#to remove courses
#remove 
courses.remove('maths')
print(courses)
#pop-remove last value of list an dit returns the value that is removed
popped=courses.pop()
print(popped)
print(courses)
#how to reverse list
courses.reverse()
print(courses)
#4. SORTING
# ascending
courses.sort()
print(courses)
num=[4,3,5,6,1,2]
num.sort()
print(num)
#descending
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)
#sort without altering original list
courses3 = sorted(courses)
print(courses3)
#min max sum
print(min(num))
print(max(num))
print(sum(num))
#5. finding value
#index
print(courses.index('computer'))
#6. LOOPING VALUES
#to check course is present or not
print('chemistry' in courses )
print('physics' in courses )
#to print all items of list
#-without index
courses4 = ['chemistry','physics','electrical','maths','computer']
for item in courses4:
 print(item)
 #-with index
for index, item in enumerate(courses4):
  print(index, item)
  #--to start with specific index
for index, item in enumerate(courses4, start=1):
   print(index, item)
#7. splitting values
#to join string
courses_str = ' - '.join(courses4)
print(courses_str)
#split
new_list = courses_str.split(' - ')
print(new_list)



 