names=['David',"Joseph", "Nihal", "Nabeel", "Rabi", "Josh"]

search= ('Nabeel')

name=input('Enter the persons name you want to check: ')
if (name.lower()==name for name in names):
    print('The person your looking for is on the list.')
else:
    print('The person your looking for is not on the list')