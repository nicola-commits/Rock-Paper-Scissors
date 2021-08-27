import random
winning_possibilities = {'p':'r', 'r':'s', 's':'p'}
wins = losses = ties = 0
var_to_names = {'p':'paper', 's':'scissors', 'r':'rock'}
guess_to_var = {1:'p', 2:'s', 3:'r'} #Ik tecnically 'p', 's' and 'r' are strings and not variables, but you get the point
while True:
    print(f"Wins: {wins}, ties: {ties}, losses:{losses}")#with the f before the string whatever you put into the brackets will be transformed into a string and printed as you can see it in the code, without all those messy +s
    userguess = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
    while userguess not in ['p', 'q', 'r', 's']:
        print("Input not valid!")
        userguess = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
    #error management ^
    if userguess == 'q':
        import sys
        sys.exit()
    print(f"{var_to_names[userguess]} versus...")
    randomguess = random.randint(1, 3)
    print(f"{var_to_names[guess_to_var[randomguess]].upper()}!") #I hope you understand this
    computerguess = guess_to_var[randomguess]
    if userguess == computerguess:
        print("Tie!")
        ties += 1
        continue
    if winning_possibilities[userguess] == computerguess:
        print("You won!")
        wins += 1
        continue
    print("You lost!") #you already made both of the other possibilities do there's no point on putting an else statement
    losses += 1
