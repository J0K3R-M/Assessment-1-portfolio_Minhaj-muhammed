
names = ['David', 'Joseph', 'Nihal', 'Nabeel', 'Rabi', 'Josh']

name = input('Enter the name of the person that you want to check: ')

if name.lower() in [n.lower() for n in names]:
    print('The person you are looking for is on the list.')
else:
    print('The person you are looking for is not on the list.')
