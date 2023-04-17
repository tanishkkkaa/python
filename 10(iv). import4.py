from my_module import *
'''we can also use (from my_module import *) this asterics imports every thing at once but we usually 
dont use this because the we don't know that what is imported and which funtion is not'''
import sys
courses = ['maths', 'chemistry', 'art']
index = find_index(courses,'art')
#to see list of all directories imported
print(sys.path)
