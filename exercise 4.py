# Creating a program that asks the user answers for certain questions and evaluating those answers and providing them feedback

name = input('Enter your name: ')
print(f'Hey {name}, welcome to the quiz. You will have to provide names of the capitals for 10 European countries.')

print()
print('Question 1:')
capital = input('What is the capital of Romania? ')
if capital.lower() == 'bucharest':  # Added .lower() to ignore case sensitivity
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 2:')
capital = input('What is the capital of Turkey? ')
if capital.lower() == 'ankara':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 3:')
capital = input('What is the capital of Spain? ')
if capital.lower() == 'madrid':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 4:')
capital = input('What is the capital of Russia? ')
if capital.lower() == 'moscow':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 5:')
capital = input('What is the capital of Serbia? ')
if capital.lower() == 'belgrade':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 6:')
capital = input('What is the capital of Slovenia? ')
if capital.lower() == 'ljubljana':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 7:')
capital = input('What is the capital of Georgia? ')
if capital.lower() == 'tbilisi':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 8:')
capital = input('What is the capital of Armenia? ')
if capital.lower() == 'yerevan':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 9:')
capital = input('What is the capital of Latvia? ')
if capital.lower() == 'riga':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print()
print('Question 10:')
capital = input('What is the capital of Montenegro? ')
if capital.lower() == 'podgorica':
    print('*The answer entered is correct*')
else:
    print('*The answer entered is incorrect*')

print("~~ THANK YOU ~~")
    