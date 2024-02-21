import random

def prisoner_dilemma_round(player_decision, bot_decision):
    if player_decision == 'Cooperate' and bot_decision == 'Cooperate':
        return 3, 3
    elif player_decision == 'Cooperate' and bot_decision == 'Betray':
        return 0, 5
    elif player_decision == 'Betray' and bot_decision == 'Cooperate':
        return 5, 0
    elif player_decision == 'Betray' and bot_decision == 'Betray':
        return 1, 1

def display_leaderboard(round_num, player_points, bot_points):
    print(f"\nRound {round_num} Leaderboard:")
    
    if player_points > bot_points:
        print(f"First place: You")
        print(f"Second place: Bot")
    elif bot_points > player_points:
        print(f"First place: Bot")
        print(f"Second place: You")
    else:
        print("It's a tie!")

def main():
    player_points = 0
    bot_points = 0
    highest_score = 0  

    round_num = 0
    while True:
        round_num += 1
        print(f"\nRound {round_num}:")

    
        player_decision = input("Enter your decision (Cooperate/Betray) or 'end' to finish: ").capitalize()

        if player_decision == 'End':
            break

        
        bot_decision = random.choice(['Cooperate', 'Betray'])
        print(f"Bot's decision: {bot_decision}")


        player_payoff, bot_payoff = prisoner_dilemma_round(player_decision, bot_decision)

        
        player_points += player_payoff
        bot_points += bot_payoff

        print(f"Your payoff: {player_payoff}")
        print(f"Bot's payoff: {bot_payoff}")

        display_leaderboard(round_num, player_points, bot_points)

    print("\nGame Over!")

    if player_points > bot_points:
        print("You won!")
    elif bot_points > player_points:
        print("Bot won!")
    else:
        print("It's a tie!")

    highest_score = max(highest_score, max(player_points, bot_points))
    print(f"Highest Score: {highest_score}")

if __name__ == "__main__":
    main()


