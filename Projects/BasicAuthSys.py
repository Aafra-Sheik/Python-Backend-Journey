"""
________________________________________________
🔐 BASIC AUTHENTICATION SYSTEM (LOGIN + SIGNUP)
________________________________________________
This project demonstrates:
-Basic backend logic thinking
-Authentication flow
-Data storage using dictionaries
-Menu-driven CLI program
-Error handling basics

The concepts used are:
-Dictionaries 
-Functions 
-Conditional statements 
-Loops
-Exception handling 
-Input/Output handling 
-Control flow 
-Dictionary methods 
-Logical and membership operations
-Basic authentication logic 
___________________________________________________
"""

users = {'Abhijith ':'2024033352', 'Maurya':'2024033362', 'Charan':'2024034169', 'Siddharth':'2024034209','Sai':'2024034327','Vamshi':'2024034458','Fanidhar':'2024034466','Mounika':'2024034714','Srikar':'2024034896' }
def login():                            #-----------------> Defining Login function
    uname = input('Username : ')
    pwd = input('Password : ')
    if uname in users and  users[uname]==pwd :  # Valid user
            print('✅ User Authorized')
    else:
            print('❌ Credentials invalid')     #Invalid user

def signup():                           #-----------------> Defining Signup function
    n_uname = input('Enter your username : ')
    if n_uname in users:
        print('This user already exists ')  # Avoids username duplication 
        return
    n_pwd = input('Enter your password : ')
    users.update({ n_uname : n_pwd })       # Updates the dictionary
    print('Signup Successful! ✔️')
    # for user , pwd in users.items():
    #      print ( f'{user}: {pwd}' )
    # users.popitem()

def main():                             #-----------------> Defining the main function
    while True:
        print( '1 : Login ')
        print( '2 : Signup ')
        print( '3 : Exit ')
        
        try:
             uinput = int(input('Select an option from the above to proceed : '))
        except:
             print('⚠️ Please enter a valid option....')    # For cases when the input is neither '1' , '2' or '3'

        if (uinput == 1):
            return login()
        elif (uinput == 2):
            return signup()
        else :
            break                       #-----------------> Exits from the program , since '3 : Exit'


main()