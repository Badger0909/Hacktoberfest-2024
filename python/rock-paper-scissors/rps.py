import random
# initialize variables

wins = 0
total_games = 0
playing = True
outcomes = ["rock", "paper", "scissors"]
# Playing loop
while playing:
    print(f"You won {wins} out of {total_games} games!")
    print("Choose Rock, Paper, or Scissors:")
    player1_input = input().lower()

    # Makes sure your input had correct capitalization
    while player1_input not in outcomes:
        print("Please try again")
        player1_input = input()
    
    # Computer's choice
    player2_input = random.choice(outcomes)
    print(f"Computer picked {player2_input}")

    # Determine the outcome
    if player1_input == player2_input:
        print("It's a tie!")
    elif outcomes.index(player2_input) == (outcomes.index(player1_input) + 1)%3:
        print("You lose!")
    else:
        print("You win!")
        wins += 1

    total_games += 1  # Increment total games for every round played

    # Ask if the player wants to play again
    print("Would you like to play again? (Y/N)")
    answer = input()
    if answer.upper() != "Y":
        playing = False
# Final message
print("Thanks for playing!")
print(f"You won {wins} out of {total_games} games!")
