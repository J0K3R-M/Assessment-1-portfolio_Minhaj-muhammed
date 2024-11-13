correct_password='10245'
max_try=5
tries=0

while tries < max_try:
    pswrd=input('Enter the Password: ')

    if pswrd==correct_password:
        print('ACCESS GRANTED. **Welcome**') 
    else:
        tries+=1
        left_tries=max_try-tries
        if left_tries>0:
            print(f'Incorrect Password. Please try again. Remaining {left_tries} attempts .')
        else:
            print('Incorrect Password. You have reached maximum limit of attempts. The organization has been infromeds for further needs contact the IT department')