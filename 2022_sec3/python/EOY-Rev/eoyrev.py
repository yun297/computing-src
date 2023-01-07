import random

stats = {
    "Wins": 0,
    "Losses": 0,
    "Draws": 0
}

for i in range(5):
    
    userinput = input("Enter rock, paper or scissors: ").lower()

    botinput = random.choice(["rock", "paper", "scissors"])
    
    
    if userinput == botinput:
        print("Draw\n")
        stats["Draws"] += 1 
    elif userinput == "rock":
        if botinput == "paper":
            print("Lose\n")
            stats["Losses"] += 1
        elif botinput == "scissors":
            print("Win\n")
            stats["Wins"] += 1

    elif userinput == "paper":
        if botinput == "rock":
            print("Win\n")
            stats["Wins"] += 1
        elif botinput == "scissors":
            print("Lose\n")
            stats["Losses"] += 1

    elif userinput == "scissors":
        if botinput == "rock":
            print("Lose\n")
            stats["Losses"] += 1
        if botinput == "paper":
            print("Win\n")
            stats["Wins"] += 1
        
print(f"Wins: {stats['Wins']} | Losses: {stats['Losses']} | Draws: {stats['Draws']}")