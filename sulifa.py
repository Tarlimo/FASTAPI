import random
import time

player_point = 0
computer_point = 0

while True:
    play = input("Want to play rock/paper/scissors?\nType yes or no: ").lower()
    if play == "no":
        break
    else:
        print("Invalid choice. Try again")
    
    instruments = ["rock", "paper", "scissors"]
    
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    

    
    def players_move():
        while True:
            player_choice = input("Choose your move: \nRock; \nPaper; \nScissors;\n").lower()
            if player_choice in instruments:
                print(f"Great! You picked {player_choice}")
                return player_choice
            else:
                print("Invalid choice. Try again")
    
    def computer_move():
        computer_choice = random.choice(instruments)
        for i in range(1,3+1):
            print("Python is thinking... ", i)
            time.sleep(1)
        print(f"Python picked: {computer_choice}")
        return computer_choice        
    
    
    def winner_logic(player, computer):
        global player_point, computer_point
        if computer in beats[player]:
            player_point += 1
            return f"You win! Your score {player_point}"
        elif player == computer:
            return "This is Tie"
        else:
            computer_point += 1
            return f"Python win! Python score {computer_point}"
        

    player = players_move()
    computer = computer_move()
    
    
    result = winner_logic(player, computer)
    print(result)
    
    


        
    