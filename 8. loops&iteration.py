#for loop

#to print items using loop
nums=[1,2,3,4,5]
for num in nums:
 print(num)

#break
for num in nums:
 if num == 3:
  print('found!')
  break
 print(num) 

#continue
nums=[1,2,3,4,5]
for num in nums: 
 if num == 3:
  print('found')
 print(num)

#loop within a loop 
for num in nums:
 for letters in 'abcd':
  print(num,letters)

#to run through a loop number of times
for i in range(10):#starts from 0 till 9
 print(i)

for j in range(1,11):#starts from 1 till 10
 print(j)

 #while loop

#
 x=0
 while x<10:
   if x==5:
    break
   print(x)
   x+=1

x=0
while True:
  if x==5:
   break
  print(x)
  x+=1

# #to create infinite loop
# x=0
# while True:
#  print(x)
#  x+=1
