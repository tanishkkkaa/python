import sys
#this way is not good
#sys.path.append('/home/taanishikaa/Desktop/My-Module')
from my_module import *
courses = ['maths', 'chemistry', 'art']
index = find_index(courses,'art')
print(sys.path)

#another way
