#allows us to interact with the underlying operating system in several different ways
'''Eg:- we can nevigate the file system
get file information
look up and change the environment variables
moves file around and all kind of useful stuff'''
import os
print(dir(os)) 
'''this shows us all of the attributes and method 
that we have access to within this module'''
print(os.getcwd())
os.chdir('/home/taanishikaa/Desktop/')#changes cwd
print(os.getcwd())#will give new changed cwd
print(os.listdir())#gives the list of all the directories(files and folders) at cwd



#creating folders
'''os.mkdir('OS-demo')#creates only the rightmost directory of path
os.makedirs('OS-Demo-2/Sub-Dir-1')#creates all directories that are part of path and do not yet exist
print(os.listdir())

os.mkdir('OS-Demo-3/Sub-Dir-1')#will give error because it cannot create sub directories and only creates right most directory of path'''



#remove folders
'''os.rmdir('OS-demo')
os.removedirs('OS-Demo-2/Sub-Dir-1')
print(os.listdir())'''



#rename
'''os.rename('mynotes.txt', 'notes.txt')
print(os.listdir())'''



#print all the information abt file
print(os.stat('notes.txt'))
print(os.stat('notes.txt').st_size)#gives size of file
print(os.stat('notes.txt').st_mtime)#gives last modification time
#to see modification time in human language
from datetime import datetime
mod_time= os.stat('notes.txt').st_mtime
print(datetime.fromtimestamp(mod_time))



#walk
'''it is a generator that yiedls a tuples of three values as its walking the  directory tree
for each directory it yields the directory path, the directory within that path and the files within that path'''
for dirpath, dirnames, filenames in os.walk('/home/taanishikaa/Desktop/'):
    print('current path', dirpath)
    print('directories', dirnames)
    print('files', filenames)
    print()#changes line



#environment variable
print(os.environ.get('HOME'))
#to create a file within home directory
file_path = '/home/taanishikaa' + 'test.txt'
print(file_path)#in this method we can forget to add slash where needed

#another method to add file at location
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)#their is no need to add slash


#other some attributes of os
#1 to grab file name of any path which can also be a fake path 
print(os.path.basename('/temp/test.txt'))#base name
print(os.path.dirname('/temp/test.txt'))#directory name
print(os.path.split('/temp/test.txt'))#to get both directory name and basename
print(os.path.exists('/temp/test.txt'))#to see wether the path exists or not
print(os.path.splitext('/temp/test.txt'))#to seperate path and extension

#to check wether it is a directory or file
print(os.path.isdir('/temp/skjghdfdf'))#true for directory
print(os.path.isfile('/temp/skjghdfdf'))#true for file

#to see everything that is available within through this os path module
print(dir(os.path))








