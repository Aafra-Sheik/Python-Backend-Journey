"""***************************************************
Project 1: Basic Chatbot
Concepts used:
- if-else
- while loop
- try-except
- input/output
***************************************************"""
bot_name: str ='Mythus'
print(f'Hello there! I am {bot_name}')

while True:
    user_input: str = input('You : ').lower()
    if user_input in ['hi' ,'hello' , 'yo']:
        print(f'{bot_name} : Hi , How can i assist you?')
    elif user_input in ['bye' , 'goodbye' ]:
        print(f'{bot_name} : Goodbye, Have a great day ahead!')
    elif user_input in ['+','add']:
        print(f'{bot_name} : Performing addition on two integers, kindly enter the values below:')
        try:
            num1: float = float(input('enter the first no: '))
            num2: float = float(input('enter the second no: '))
            print(f'{bot_name} : The sum of {num1} and {num2} is {num1+num2}')
        except ValueError:
            print(f'{bot_name} : Oops! please enter a valid numerical format')
    elif user_input in ['-','sub','subtract']:
        print(f'{bot_name} : Performing subtraction on two integers, kindly enter the values below:')
        try:
            num1: float = float(input('enter the first no: '))
            num2: float = float(input('enter the second no: '))
            print(f'{bot_name} : The difference of {num1} and {num2} is {num1-num2}')
        except ValueError:
            print(f'{bot_name} : Oops! please enter a valid numerical format')
    elif user_input in ['*','mul','multiply']:
        print(f'{bot_name} : Performing multiplication on two integers, kindly enter the values below:')
        try:
            num1: float = float(input('enter the first no: '))
            num2: float = float(input('enter the second no: '))
            print(f'{bot_name} : The product of {num1} and {num2} is {num1*num2}')
        except ValueError:
            print(f'{bot_name} : Oops! please enter a valid numerical format')
    elif user_input in ['/','div','division']:
        print(f'{bot_name} : Performing division on two integers, kindly enter the values below:')
        try:
            num1: float = float(input('enter the first no: '))
            num2: float = float(input('enter the second no: '))
            print(f'{bot_name} : The quotient of {num1} and {num2} is {num1/num2}')
        except ValueError:
            print(f'{bot_name} : Oops! please enter a valid numerical format')
    elif user_input in ['%','rem','remainder','mod']:
        print(f'{bot_name} : Performing modulus on two integers, kindly enter the values below:')
        try:
            num1: float = float(input('enter the first no: '))
            num2: float = float(input('enter the second no: '))
            print(f'{bot_name} : The remainder of {num1} and {num2} is {num1%num2}')
        except ValueError:
            print(f'{bot_name} : Oops! please enter a valid numerical format')

    else:
        print(f'{bot_name} : Sorry, i am not able to understand that . Please try again...')