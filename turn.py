coins =21
def play_human_turn(n):
    # 1. prompt user for their move 
    while coins != 0: 
        usercoins=int(input('How many coins do you want to take? 1, 2 or 3: '))
        if usercoins == 1 or usercoins ==2 or usercoins==3: 
    # 2. output number of coins after user's move
            new = n-usercoins
            if new == 0:
                print('The number of coins left now are 0. You win!')
                return 0
        # 3. If the human wins, indicate that and return 0 
            print(f'The number of coins left now are {new}')
            return new
        else: 
            print('Invalid coin amount please try again')
    # You must implement this function
#play_human_turn(coins)



import random 
def play_computer_turn(c):
    # 1. Make computer move
    if c % 4 == 0:
        take_coins = random.randint(1, 3)
    else:
        take_coins = c % 4

    newc = c - take_coins
    if newc == 0: 
        print(f'The computer took {take_coins}, there are 0 coins left. Computer wins!')
        return 0
    # 2. If computer wins, indicate that and return 0
    print(f'The computer took {take_coins}, there are {newc} coins left.')
    return newc
    # 3. return number of coins remaining
   
    # You must implement this function 
#play_computer_turn(coins)
