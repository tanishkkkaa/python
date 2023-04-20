message = 'hello'
print(message)
#to print with number of single quotes in string
message = 'hello\'s'
print(message)
message = "hello's"
print(message)
#print multiple line string
message = """hello
world"""
print(message)
#print lenght of our message
message = 'hello'
print(len(message))
#print individual letter
message = 'hello'
print(message[3])
#error
#message = 'hello'
#print(message[5])
#print range of letters
message = 'hello'
print(message[0:4])
message = 'hello'
print(message[:3])
message = 'hello'
print(message[2:])
#how to change case
message = 'hello'
print(message.upper())
message = 'hello'
print(message.lower())
#how to count number of alphabet in word
message = 'hello'
print(message.count('h'))
message = 'hello'
print(message.find('llo'))
message = 'hello'
print(message.find('world'))
#replace
message = 'hello world'
message = message.replace('world','universe')
print(message)
message = 'hello'
print(message)
#addition of string
greeting = 'hello'
name = 'Arishka'
message = greeting + name
print(message)
#addition of string with space
greeting = 'hello'
name = 'Arishka'
message = greeting +  ', my name is ' +name
print(message)
#easy method for long string 1
greeting = 'hello'
name = 'Arishka'
message = '{}, my name is {}'.format(greeting, name)
print(message)
#easy method for long string 2
greeting = 'hello'
name = 'Arishka'
message = f'{greeting}, my name is {name.upper()}'
print(message)
#broad overview of all the attributes and methods that are available to you now
print(dir(name))
#easy method for long string 1
greeting = 'hello'
print(help(str))
print(help(str.lower))
#to reverse a string
print(message[::-1])