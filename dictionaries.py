student = {'name': 'Tanishka', 'age': 19, 'courses': ['computer', 'maths']}
print(student)

print(student['courses'])
print(student['age'])
print(student['name'])
#error print(student['phone'])

print(student.get('name'))
print(student.get('phone'))#returns none
print(student.get('phone', 'not_found'))#returns not found

#to add 
student['phone'] = '5555-24333'
print(student)

#if we change info
student['name'] = 'Tanu'
print(student)

#to update info in one shot
student.update({'name': 'tanya', 'age': 20, 'phone': '66666-45454'})
print(student)

#remove key or value
del student['phone']
print(student)

age = student.pop('age')
print(student)
print(age)

#to find number of keys
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())#for both key and values

#looping
for keys in student:
 print(keys)

for keys,value in student.items():
 print(keys,value)