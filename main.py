from proj import MENU,resources

while True:
    choice = input('What would you like? (espresso/latte/cappuccino):')

    if choice == 'report':
        print('water',resources['water'])
        print('milk',resources['milk'])
        print('coffee',resources['coffee'])

    elif choice == 'espresso':
        if resources["water"] < MENU['espresso']['ingredients']['water'] or resources["coffee"] < MENU['espresso']['ingredients']['coffee']:
            print('out of stock')
            break

        print('Insert coins')
        quater = int(input('number of quarters:'))
        dimes = int(input('number of dimes:'))
        nickles = int(input('number of nickles:'))
        pennies = int(input('number of pennies:'))

        given = 0.25 * quater + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        price = 1.5

        change = given - price
        print('your change',round(change,2))

        if change < 0:
            print('less money')


        elif change > 0:
            print('here is you espresso!')

            resources["water"] = resources["water"] - MENU['espresso']['ingredients']['water']
            # resources["milk"] = resources["milk"] - MENU['espresso']['ingredients']['milk']
            resources["coffee"] = resources["coffee"] - MENU['espresso']['ingredients']['coffee']

    elif choice == 'latte':
        if resources["water"] < MENU['latte']['ingredients']['water'] or resources["milk"] < MENU['latte']['ingredients']['milk'] or resources["coffee"] < MENU['latte']['ingredients']['coffee']:
            print('out of stock')
            break

        print('Insert coins')
        quater = int(input('number of quarters:'))
        dimes = int(input('number of dimes:'))
        nickles = int(input('number of nickles:'))
        pennies = int(input('number of pennies:'))

        given = 0.25 * quater + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        price = 2.5

        change = given - price
        print('your change',round(change,2))

        if change < 0:
            print('less money')


        elif change > 0:
            print('here is you latte!')

            resources["water"] = resources["water"] - MENU['latte']['ingredients']['water']
            resources["milk"] = resources["milk"] - MENU['latte']['ingredients']['milk']
            resources["coffee"] = resources["coffee"] - MENU['latte']['ingredients']['coffee']



    elif choice == 'cappuccino':
        if resources["water"] < MENU['cappuccino']['ingredients']['water'] or resources["milk"] < MENU['cappuccino']['ingredients']['milk'] or resources["coffee"] < MENU['cappuccino']['ingredients']['coffee']:
            print('out of stock')
            break

        print('Insert coins')
        quater = int(input('number of quarters:'))
        dimes = int(input('number of dimes:'))
        nickles = int(input('number of nickles:'))
        pennies = int(input('number of pennies:'))

        given = 0.25 * quater + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        price = 3

        change = given - price
        print('your change',round(change,2))

        if change < 0:
            print('less money')

        elif change > 0:
            print('here is you cappuccino!')

            resources["water"] = resources["water"] - MENU['espresso']['ingredients']['water']
            resources["milk"] = resources["milk"] - MENU['espresso']['ingredients']['milk']
            resources["coffee"] = resources["coffee"] - MENU['espresso']['ingredients']['coffee']