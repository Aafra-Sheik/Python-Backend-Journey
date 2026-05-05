"""
DAY 4: FUNCTIONS
_______________________________
-FUCTIONS
-TYPES OF FUCTIONS
-RECURSION
-PRACTISE QUESTIONS
_______________________________
"""
#Funtions :  reduces redundancy of the code 
def sum(a,b):  # ------> a & b are 2 params 
    s = a+b
    return s
print(sum(2,1))   # -------> 1 & 2 are args 

#types of functions-------built in
                    #   |        |__print
                    #   |        |__len
                    #   |        |__type
                    #   |        |__range
                    #    ---user deifined

#waf to print the length of the list 
cities=['hyderabad','delhi','mumbai','gurgaon']
def length_cities(list):
    print(len(list))
length_cities(cities)
'''*******************'''
#waf to print the elements of the list in single line 
cities=['hyderabad','delhi','mumbai','gurgaon']

def lin_el(list):
    for i in list:
     print( i , end=' ')
lin_el(cities)

#waf to find the factorial of n ( param = n )
n = int(input('enter the value : '))
def fact(n):
    prod=1
    for i in range(1,n+1):
        prod*= i
    print(prod)
fact(n)

#waf to convert usd to inr 
usd = int(input('enter the amount in $ :'))
def ind(usd):
    ind= usd * 95.350
    print(ind)
ind(usd)

#waf to identify if a num is even or odd
n = int(input('enter a number : '))
def odorev(n):
    if ( n % 2 == 0):
        return 'EVEN'
    else :
        return 'ODD'
print(odorev(n))

'''****************************************'''
#Recursion: its a function that calls itself , forms a call stack
n = int(input('enter a number : '))
def show(n):
    if (n==0):          # base case / stopping cond
        return 
    print(n)
    show(n-1)               
show(n) 

#factorial through recursion
n = int(input('enter a number : '))
def fact_rec(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact_rec(n-1) * n
print(fact_rec(n))

#warf to find the sum of first n natural numbers
n = int(input('enter a number : '))
def sum(n):
    if (n==0):
        return 0
    else:
        return n + sum (n - 1)
print(sum(n))

#warf to print all elements in the list (params are list and index)
cities=['hyderabad','delhi','mumbai','gurgaon']
def el( list):
    for i in list:
     if (i ==len(list)):
         return
     else :
         print(i)
print(el(cities))