#true and false values are known as booleans
language = 'JavaScript'
if language == 'python':
 print('language is python')
elif language == 'java':
 print('language is java')
elif language == 'JavaScript':
 print('language is JavaScript')
else:
 print('no match')

#and or not

#and
user = 'admin'
logged_in = False
if user == 'admin' and logged_in:
  print('admin page')
else:
  print('bad creds')

#or
user = 'admin'
logged_in = False
if user == 'admin' or logged_in:
  print('admin page')
else:
  print('bad creds')

#not
if not logged_in:
   print('please log in')
else:
   print('welcome')

#==
a = [1,2,3]
b = [1,2,3]
c = b
print(a==b)
print(id(a))
print(id(b))
print(a is b)
print(b is c)#print(id(a)==id(b))

#False values

#false
condition = False
if condition:
  print('condition is true')
else:
  print('condition is false')

#none
condition = None
if condition:
  print('condition is true')
else:
  print('condition is false')

#zero of any numeric type
condition = 0
if condition:
  print('condition is true')
else:
  print('condition is false')

condition = 10#true
if condition:
  print('condition is true')
else:
  print('condition is false')

#any empty sequence '',(),[]
condition = ()
if condition:
  print('condition is true')
else:
  print('condition is false')

condition = 'test'
if condition:
  print('condition is true')#true
else:
  print('condition is false')

#any empty mapping {}
condition = {}
if condition:
  print('condition is true')
else:
  print('condition is false')
