"""
DAY 3: LOOPS
_______________________________
-WHILE
-BREAK / CONTINUE / PASS
-FOR
-RANGE
-LIST ENUMERTAION
-ZIP
-PRACTISE QUESTIONS
________________________________"""

# while True:
#     print ('hello')   #infinite loop 

count =1  #intitial value 
while count<= 5:  #condition aded to tell where to stop 
   print('hello')
   count += 1 #updating                                            #while loop with conditions for breaks
print(count)   #return the count value where the loop breaks

"""**********************************"""
#print numbers 1 to 100
i = 1
while i<=100:
    print(i)
    i += 1
print('***********')

#print numbers from 100 to 1 
i=100
while i>=1:
    print(i)
    i-=1
print('***********')

#print muliptication table of n 
n= int(input('enter n:'))
i=1
while i<=10:
    print(i*n)
    i+= 1
print('***********')

#print the element of the following list udint loops - [1,4,9,16,25,36,49,64,81,100]
list = [1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(list):
    print(list[i])
    i += 1
print('***********')

#search for  number x in this tuple using loop:
tuple = (1,4,9,16,25,36,49,64,81,100)
n= int(input('enter the element to search: '))
i=0 
while i<len(tuple):
    if ( tuple[i] == n):
        print('element found at ' ,i)
    i+=1
print('***********')

"""**********************************"""
i=1
while i<=5:
    print(i)
    if(i==3):
        break            #breaks the loop
    i+=1
print('***********')

i=1
while i<=10:
    
    if(i==5):
        i +=1 
        continue            #skipping
    print(i)
    i += 1
"""**********************************"""
india = ['hyderabad','delhi','mumbai','kochi','vizag']
for city in india:
    print(city)

name = 'delhi'
for char in name :
    print(char)

#using for :print the element of the following list udint loops - [1,4,9,16,25,36,49,64,81,100]
list = [1,4,9,16,25,36,49,64,81,100]

for num in list:
    print (num)

# ising for : search for  number x in this tuple using loop:
tuple = (1,4,9,16,25,36,49,64,81,100)
x= int(input('enter element to search: '))

i=0
for n in tuple :
    if (n==x):
     print('element found at index',i)
     break
    i+=1
"""**********************************"""
for i in range (10):           # stop
    print(i)
print('***********')
for i in range (5,10):          # start,stop
    print(i)
print('***********')
for i in range (2,10,2):        # start,stop,inc
    print(i)

#using for and range: print numbers 1 to 100
for i in range (1,101,1):
    print(i)
    
#using for and range: print numbers 100 to 1
for i in range (100,0,-1):
    print(i)
    
#print muliptication table of n 
n= int(input('enter n:'))
for i in range (1,11):
    print(i*n)
"""**********************************"""
#pass  ---> placeholder for future code 
"""**********************************"""
#wap to find the sum of first n num using while 
n= int(input('enter the value for n : '))
sum = 0
i=1
while i<=n:
    sum +=i
    i+=1
# for i in range(1,n+1):
#     sum += i
print("total is :", sum)

#wap to find the factorial of first n int using for 
n= int(input('enter the value for n : '))
fact=1
for i in range(1,n+1):
    fact*=i
print('the factorial is:', fact)
"""**********************************"""
#List enumeration
team=['aafra','sony','wazid','charli']
for index , emp in enumerate(team):         #coverts the list into pairs of index and value
    print(index ,emp)
"""**********************************"""
#Zip()-----> combines multiple  lists
name = ['aafra','sony','wazid','charli']
marks = [80,90,90,60]
for i,j in zip(name , marks):
    print(i,j)

res_list = list(zip(name , marks))
print(res_list)                #-------> coverting zip to list

res_dict = dict(zip(name , marks))
print(res_dict)                #-------> coverting zip to dictionary