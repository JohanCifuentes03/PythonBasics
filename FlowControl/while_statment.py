import sys

condition = input('Do you want to enter to the menu? (y/n) ').lower().strip()
money = 0

while condition == 'y':
    option = int(input("Menu:\n1.See money\n2.Add money\n3.Take out money\n4.exit\n"))
    if option == 1:
        print("Your money is: ", money)
    elif option == 2:
        extra_money = float(input('Enter the money: '))
        money = money + extra_money
    elif option == 3:
        out_money = float(input('Enter the money: '))
        if out_money > money:
            print("not enough money")
            continue
        else:
            money = money - out_money
    elif option == 4:
        sys.exit()
    condition = input("Do you want to continue? (y/n) ").lower().strip()
print("Thank you!!")