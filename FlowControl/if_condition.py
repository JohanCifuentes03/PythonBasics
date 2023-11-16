name = input('Enter your name: ')
age = int(input('Enter your age:'))

if name == 'Johan':
    print('Hello boss, please enter')
else:
    print(f'Hello {name}')
    if age < 18:
        print('You are not allowed to enter here, get out of here!!')
        print('or... do you have some money? ')
        money = float(input("How much money do you have? "))
        if money < 100:
            print("Not enough, get out of here!!")
        else:
            print("Mmmmm, you can pass")