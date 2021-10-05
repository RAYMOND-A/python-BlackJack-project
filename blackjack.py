import random

def compare(user_score, computer_score):
    if user_score == computer_score:
        return f"it is a draw"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def calculate_score(cards):
    """Takes a list of cards and return the score calculated from the cards"""
    # check for a blackjack (a hand with only 2 cards: ace and 10) and return 0 instead
    # of the actual score. 0 will represent a blackjack in our game
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # check for an 11 (ace). if the score is already over 21, remove the 11 and replace
    # it with a 1. you might need to look up append() and remove()
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

blackjack_art = '''
 ___   ___
|A  | |10 |
| ♣ | | ♦ |
|__A| |_10|
'''

def play_game():
    print(blackjack_art)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        computer_cards.append(new_card)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" your cards: {user_cards} and current score: {user_score}")
        print(f" computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0  or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Ask user if they want to restart the game. if they answer yes, clear the console
# and start a new game of blackjack and show the logo from art.py

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()

