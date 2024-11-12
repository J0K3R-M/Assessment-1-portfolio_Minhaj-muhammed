# creating a program that asks the user answers for certain questions and evaluating those answers and providing them a feedback 

'''ADVANCED REQUIREMENTS'''

name=input('Enter your name: ')
print('Hey',name,'Welcome to the quiz, you will have to provide names of the capital states for 10 European Countries')

print() #added an empty print statement.
print('Question 1:')
capital=input('Whats the Capital of Romania: ') #the program where the user can view the question and provide the suitable answer
if(capital.lower()=='Bucharest'): #added .lower so that the python code makes the specific statement uppercase to lowercase.
    print('*The answer entered is correct*') 
else:
    print('*The answer entered is incorrect*')

print()
print('Question 2: ')
capital=input('Whats the Capital of Turkey: ')
if(capital.lower()=='Ankara'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 3: ')
capital=input('Whats the Capital of Spain: ')
if(capital.lower()=='Madrid'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 4: ')
capital=input('Whats the Capital of Russia: ')
if(capital.lower()=='Moscow'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 5: ')
capital=input('Whats the Capital of Serbia : ')
if(capital.lower()=='Belgrade'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 6: ')
capital=input('Whats the Capital of Slovenia: ')
if(capital.lower()=='Ljubljana'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 7: ')
capital=input('Whats the Capital of Georgia: ')
if(capital.lower()=='Tbilisi'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 8: ')
capital=input('Whats the Capital of Armenia: ')
if(capital.lower()=='Yerevan'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 9: ')
capital=input('Whats the Capital of Latvia: ')
if(capital.lower()=='Riga'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 10: ')
capital=input('Whats the Capital of Montenegro: ')
if(capital.lower()=='Podgorica'):
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print("****THANK YOU****")