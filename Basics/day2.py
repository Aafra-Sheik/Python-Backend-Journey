"""
DAY 2:LISTS & DICTIONARIES
_______________________________
-LISTS --> mutable and flexible
-TUPLES --->immutable and faster
-SETS ---> mutable (add/remove),  unordered, cant access by index ,no dupes , best for membership testing , no append only add but added element can fall anywhere 
-DICTIONARIES
________________________________
"""
#LISTS:
fruits = ['apple','orange','mango','kiwi']
print(fruits)       #displays content as array
for fruit in fruits:
    print(fruit ,end=' ')       #displays seperately and looks more cleaner

print(fruits[2])        #accessing an element through index number

fruits[3] = 'banana'        #modifying the list by index 
 
fruits.append('coconut')        #adds this as a new element to the last of the list

fruits.remove('mango')          #removes this element from the list

fruits.pop(2)            #removes only but by index no

fruits.clear()          #removes all emelents from the list

#TUPLES
#cant change elements or modify 
#cant append
#cant remove
#used when u have a collection that cant be changed 

#SETS:
#no item assignments beacuse order keeps changing
#indexing isnt a priority
fruits = {'apple','orange','mango','kiwi'}
print(fruits)       #displays content as array
for fruit in fruits:
    print(fruit ,end=' ')

if 'apple' in fruits:           # membership test - searching for element in a set 
    print('apple was found')
else:
    print('apple was not found')

#DICTIONARIES:
#stores as key value pairs
capitals = { 'India' : 'Muscat' , 'Oman' : 'Muscat' , 'Russia' : 'Moscow' ,'Germany' :'Berlin' }
print(capitals)

print(capitals.get('Oman'))

#Looping 
if capitals.get('Germany'):
    print('capital exists')
else:
    print('capital does not exist')

#updating
capitals.update({'India' : 'Delhi'})

#deleting using key 
capitals.pop('Germany')

#deleting the latest item
capitals.popitem()

#deleting all the data in dictionaries 
capitals.clear()

#accessing only keys 
keys = capitals.keys()
for key in capitals.keys():
    print(key)

#accessing only values 
values = capitals.values()
for value in capitals.values():
    print(value)

#accessing keys and values
items = capitals.items()
for key, value in capitals.items():
    print(f'{key}: {value}')