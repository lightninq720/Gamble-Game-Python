import random
money = 500
print('Welcome to the gambling game!')
loop = True
while loop == True:
    try:
        print('You have $' + str(money))
        bet = int(input('How much do you want to bet? '))
        if bet > money:
            print('Invalid Bet')
        elif bet <= 0:
            print('Invalid bet')
        else:
            chance = random.randint(1,2)
            if chance == 1:
                print('You Won!')
                money += bet
            else:
                print('You Lost!')
                money -= bet
    except ValueError:
        print('Invalid Bet')
