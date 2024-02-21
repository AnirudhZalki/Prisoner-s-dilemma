from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "os.urandom(24)" 

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

def update_game_state(player_choice):
    # Check if session exists for game state
    if 'game_state' not in session:
        session['game_state'] = {'round_num': 0, 'player_points': 0, 'bot_points': 0, 'highest_score': 0}

    game_state = session['game_state']
    round_num = game_state['round_num'] + 1
    game_state['round_num'] = round_num

    bot_choice = random.choice(['Cooperate', 'Betray'])
    player_payoff, bot_payoff = prisoner_dilemma_round(player_choice, bot_choice)

    game_state['player_points'] += player_payoff
    game_state['bot_points'] += bot_payoff
    game_state['highest_score'] = max(game_state['highest_score'], max(game_state['player_points'], game_state['bot_points']))
    game_state['bot_choice'] = bot_choice  # Added this line to store bot's choice

    return game_state, round_num, player_payoff, bot_payoff

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play_round():
    player_choice = request.form["choice"]
    game_state, round_num, player_payoff, bot_payoff = update_game_state(player_choice)

    return render_template("index.html", 
                           round_num=round_num, 
                           player_choice=player_choice, 
                           bot_choice=game_state['bot_choice'],  # Corrected this line
                           player_payoff=player_payoff, 
                           bot_payoff=bot_payoff, 
                           **game_state)

if __name__ == "__main__":
    app.run(debug=True)



