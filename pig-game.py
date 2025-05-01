import random


def roll_dice():
    """Simulates rolling two dice by calling randint two times.
    Both dice can only be integer values from 1 to 6."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def computer_turn(game_score, goal):  
    """Simulates one turn for the computer until the turn total
    is less than the goal, one die is one, or
    both dice are one. If one of the dice is 1 the turn total
    is reset to 0, but not the game score. If
    both dice are one both the game score and turn total are reset
    to 0. if the dice are not 1 they get added to the previous turn total."""

    turn_total = 0
    while turn_total < goal:
        die1, die2 = roll_dice()
        if die1 == 1 and die2 == 1:
            game_score = 0
            turn_total = 0
            print(f'Computer rolled {die1, die2} Turn total: {turn_total}')
            break
        elif die1 == 1 or die2 == 1:
            turn_total = 0
            print(f'Computer rolled {die1, die2} Turn total: {turn_total}')
            break
        else:
            turn_total = turn_total + die1 + die2
            print(f'Computer rolled {die1, die2} Turn total: {turn_total}')
    game_score += turn_total
    return game_score

def human_turn(game_score): 
    """Allows a human to play until the turn total is
    greater than or equal to 100, both dice are 1, one die is 1,
    or the person ends the turn by typing n. If the turn total is greater
    than or equal to 100 the previous game score is added to the turn total.
    If both dice are 1 the game score and turn total are reset to 0. When one of
    the dice is 1 the turn total is reset to 0. If the person chooses to end their
    turn the game score is added to the previous game score and the turn total."""

    h_turn = True  # is it the humans turn? true = y false = n
    h_turn_total = 0
    while h_turn:
        die1, die2 = roll_dice()
        if h_turn_total >= 100:
            game_score += h_turn_total
            break

        elif die1 == 1 and die2 == 1:
            h_turn_total = 0
            game_score = 0
            print(f'You rolled {die1, die2} Turn total: {h_turn_total}')
            break
        elif die1 == 1 or die2 == 1:
            h_turn_total = 0
            print(f'You rolled {die1, die2} Turn total: {h_turn_total}')
            break
        else:
            h_turn = True
            h_turn_total = h_turn_total + die1 + die2
            print(f'You rolled {die1, die2} Turn total: {h_turn_total}\n')
            user_chose = validate_response('Roll again (y/n)? ', 'y', 'n')
            if user_chose.lower() == 'n':
                game_score += h_turn_total
                break
    return game_score

def human_vs_computer():  # human goes first then computer
    """Allows the human to play a game against the computer until
    the human score is greater than 100 and the computer score or computer
    score is greater than 100 and the human score. If the human score is greater
    than 100 and the computer score the human won the game. If the computer score
    is greater than 100 and the human score the computer wins the game and the human loses."""

    enter = True
    human_score = 0
    computer_score = 0
    while enter:
        human_score = human_turn(human_score)
        computer_score = computer_turn(computer_score, 20)
        print(f'\nYou: {human_score} Computer: {computer_score}\n')
        if human_score >= 100 and human_score > computer_score:
            print('Congratulations!')
            break
        elif computer_score >= 100 and computer_score > human_score:
            print('Sorry you lost.')
            break

def computer_solo(goal):  
    """Allows one computer to play a game by itself
    until the computer score is greater than or equal to 100. If the
    computer score is greater than or equal to 100 the game ends
    and the turns are printed."""

    turns = 0
    computer_score = 0
    comp_turn = True
    while comp_turn:
        computer_score = computer_turn(computer_score, goal)

        turns += 1
        print(f'Turn: {turns} Score: {computer_score}')
        if computer_score >= 100:
            print(f'Turns: {turns}')
            comp_turn = False
    return turns

def world_championship(games, goal_1, goal_2):  
    """Allows two computers to play a game until player1 score is
    greater than player2 score or player2 score is greater than player1
    score. If player1 score is greater than player2 score, player1 wins. If
    player2 score is greater than player1 score, player2 wins."""

    player1_wins = 0
    player2_wins = 0

    for x in range(games):
        player1_score = 0
        player2_score = 0

        while player1_score < 100 and player2_score < 100:
            player1_score = computer_turn(player1_score, goal_1)
            player2_score = computer_turn(player2_score, goal_2)
        print(f'Player 1 Score: {player1_score} Player 2 Score: {player2_score}')
        if player1_score > player2_score:
            player1_wins += 1
        else:
            player2_wins += 1

    print(f'Player1: {player1_wins} wins Player2: {player2_wins} wins')
    return player1_wins, player2_wins

def validate_response(prompt, response1, response2):  
    """Checks for unacceptable input from the user. It only allows
    the user to move on when they give the correct or acceptable
    response to the prompt."""

    response = input(prompt).lower()
    while response1 != response and response2 != response:
        response = input(prompt).lower()
    return response

if __name__ == '__main__':
    choose = input('Enter computer solo, com vs com, human vs computer, or quit: ').lower()
    while choose != 'quit':
        if choose == 'computer solo':
            computer = int(input('Enter a goal: '))
            computer_solo(computer)
        elif choose == 'com vs com':
            game = int(input('Enter the amount of games to play: '))
            goal1 = int(input('Enter the first goal the computers need to meet: '))
            goal2 = int(input('Enter the second goal the computers need to meet: '))
            world_championship(game, goal1, goal2)  # provides games played and two goals
        elif choose == 'human vs computer':
            human_vs_computer()
        again = validate_response('Play again (y/n)? ', 'y', 'n')
        if again == 'y':
            choose = input('Enter: computer solo, com vs com, or human vs computer: ').lower()
        elif again == 'n':
            break
    print('You choose to end the game.')

