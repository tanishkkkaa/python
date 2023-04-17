#will print any random value using standard libraries
import random
courses = ['maths', 'chem', 'art']
random_courses= random.choice(courses)
print(random_courses)


import math
rads = math.radians(90)
print(math.sin(rads))


import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2023))
print(calendar.isleap(2024))


import os #gives access to underlying operating system
print(os.getcwd())#current working directory
print(os.__file__)#prints out location of our file on our file system


import antigravity#opens a comic