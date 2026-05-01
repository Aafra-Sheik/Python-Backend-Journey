"""
DAY 1:BASIC OF PYTHON 
_______________________________
-VARIABLES
-DATA TYPES
-TYPE CONVERSION
-TYPE ANNOTATIONS
-F-STRINGS
-IF ELSE STATEMENTS
-ERROR HANDLING
-IMPORT
-FUNCTIONS
-LOOPS
________________________________
"""
#PRINT STATEMENT:

print("Hello, Aafra!")

#VARIABLES:

name= 'Aafra'
print("Hello there " + name + "!")

"""***************************************************"""
#DATATYPES:

text='aaple'    #string

number=120      #integer

decimal=21.34   #float

has_money=True  #boolean

coordinates=(17.1,61.5)  #tuple

names=['sony','wazid','aafra']  #list

unique={1,2,3,4,4,5}  #set(no duplicates , only unique values will get printed)
print(unique)

users={1:'aafra',2:'sony',3:'wazid'}    #dictionary(key-value pairs)
print(users[3])

"""***************************************************"""
#TYPE CONVERSION:

num=100     #normal method 
print(100+num)

num_str='100'     #this will give error beccause we are doing int +str
#print(100+num_str)

num_str_tc='100'       #this is the correct way since str--->int
print(100+int(num_str_tc))

print(float('123.456'))     #directly printing output of str--->float

"""***************************************************"""
#TYPE ANNOTATIONS:

age: int = 21
name: str = 'Aafra'         #specifying the dtype during variable declaration 

"""***************************************************"""
#F-STRINGS:

age: int = 21
name: str = 'Aafra'
#print('Name:' + name + 'Age: ' + age)    #this will give error because we are trying to concatenate str with int
print('Name:' + name + ' , Age: ' + str(age))

print(f'Name:{name} , Age: {age}')  #f-string is a more efficient way to format strings and it automatically converts the variables to their string representation, so we don't need to use str() for type conversion.

"""***************************************************"""
#IF-ELSE STATEMENTS:

input:str = 'hdghxfg'  #change inputs and see
if input == 'hello':
    print('Bot: Hey! whatsup?')
elif input == 'how are you?' :
    print('Bot: I am good , what about you?')
else:
    print('Bot: Sorry , i was not able to understand that.')

"""***************************************************"""
#ERROR HANDLING:

a,b = 10 , 'five'
try:
    print(a+b)
except TypeError as e :
    print('Please enter a number as an integer only!!!')
except Exception as e :
    print('Something else went wrong...')
print('Continuing with the program....')

"""***************************************************"""
#IMPORT:

import math         #importing the math module to access mathematical functions and constants.
print(math.sqrt(36))

import math as m    #importing the math module and giving it an alias 'm' so we can use 'm' instead of 'math' to access its functions.
print(m.sqrt(25))

from math import sqrt,tan  #importing specific functions from the math module so we can use them directly without prefixing with math. or m.
print(sqrt(121))
print(tan(45))

"""***************************************************"""
#FUNCTIONS:
def  greet(name: str , greeting:str = 'Hello'): 
    print(f'{greeting},{name}!')

greet ('Aafra','Assalamu alaikum ')

"""***************************************************"""
#LOOPS:

#for ---> finite list of elements
for i in range(3):
    print('hello')      #this will print hello 3 times since we have specified the range as 3

#while ---> infinite list of elements
while True:
    print('hello')   #this will print hello infinitely until we stop it manually


i:int = 0
while i<3:         
    print(i)        #stops at the condition if false 
    i+=1                        
"""***************************************************"""