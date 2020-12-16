import random
#Creating a global loop for multiple iterations
game = "yes"
while(game == "yes"):
    print("Guess a number between 1 and 100")
    guess = 50
    upper = 100
    lower = 1
    print (f"You guessed {guess}, is it correct, low or high")
    human_reply = input("Your reply :").lower()
    while(human_reply != "correct"):
        if(human_reply == "low"):
            lower = guess+1
        elif(human_reply == "high"):
            upper = guess-1
        guess = random.randint(lower,upper)
        print(f"lower is {lower}  and upper is {upper}")
        print (f"You guessed {guess}, is it correct, low or high")
        human_reply = input("Your reply :").lower()
        print(f"human_reply{human_reply}")
    print(f" You guessed {guess}")
    game = input("Do you want to play again yes or no:").lower()