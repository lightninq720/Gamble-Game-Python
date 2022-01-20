import random, time


#vars
coins = 500
attempts = 0
successful_attempts = 0
unsuccessful_attempts = 0

#game
while True:
    if coins == 0:
        print("You have gone bankrupt!!")
        print("\nGame will end in 3 seconds")
        time.sleep(3)
        break
    print("Current Stats:")
    print("Overall Attempts:", attempts)
    print("Successful Attempts", successful_attempts)
    print("Unsuccessful Attempts:", unsuccessful_attempts)
    print(f"You have £{coins}")
    try:
        gamble = int(input("How much do you want to gamble?\n"))
        if gamble > coins:
            print("Invalid Bet")
        elif gamble <= 0:
            print("Invalid Bet")
        else:
            chance = random.randint(1,2)
            attempts += 1
            if chance == 1:
                print("You Won!")
                coins += gamble
                successful_attempts +=1
            else:
                print("You lost.")
                coins -= gamble
                unsuccessful_attempts +=1
    except ValueError:
        print("Invalid Input")


