#function-allow us to reuse our code without repeating ourselves 

#pass keyword
def hello_func():
 pass#it says that we dont want a parameter rn but will pass later
print(hello_func())

def hello_func():
 print('hello')
hello_func()

#executing function

#function reusablity
def hello_func():
 print('hello')
hello_func()
hello_func()
hello_func()
hello_func()
hello_func()

#return
def hello_func():
 return 'hello'#stores value in function
hello_func()#no output
#but if we print our function then it will give us output
print(hello_func().upper())

def hello_func(greeting):
 return '{} Function'.format(greeting)
print(hello_func('Hi'))

def hello_func(greeting, name='you'):
 return '{}, {} shutup'.format(greeting,name)
print(hello_func('Hey'))

def hello_func(greeting, name='you'):
 return '{}, {} shutup'.format(greeting,name)
print(hello_func('Hey', name='tanishka'))

#positional keyword arguments

#
def student_info(*args, **kwargs):#accepting an arbitrary number
  print(args)#tuple with positional arguments
  print(kwargs)#dictionary with keyword values
student_info('maths', 'art', name = 'tanishka', age = 19)

courses = ['maths', 'art']
info = {'name': 'tanishka', 'age': '19'}
student_info(*courses,**info)#unpacks the value