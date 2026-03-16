# Blackjack Game

"""
This module contains the implementation of a simple Blackjack game.
The game allows a user to play against a dealer, where both the player
and dealer try to get as close to 21 without going over.
"""

import random

# Define a function to calculate the score of a hand

def calculate_score(hand):
    """
    Calculate the current score of the given hand.
    The score is calculated by summing the card values.
    Aces can count as 1 or 11, depending on the current score.
    """
    score = 0
    ace_count = 0
    
    for card in hand:
        if card in ['K', 'Q', 'J']:
            score += 10
        elif card == 'A':
            ace_count += 1
            score += 11  # Initially count Ace as 11
        else:
            score += card  # For numeric cards
    
    # Adjust score for Aces if score exceeds 21
    while score > 21 and ace_count:
        score -= 10  # Count Ace as 1 instead of 11
        ace_count -= 1
    return score

# Define a function to get a random card

def deal_card():
    """
    Return a random card from the deck.
    Possible values are numbers 2-10, and 'J', 'Q', 'K', 'A'.
    """
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    return random.choice(cards)

# Define a function to play a round of Blackjack

def play_blackjack():
    """
    Main function to execute the Blackjack game.
    It handles the game flow, including dealing cards
    to the player and dealer, and determining the winner.
    """
    player_hand = []
    dealer_hand = []
    
    for _ in range(2):  # Deal two cards to each player
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    game_over = False
    
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f'    Player hand: {player_hand}, current score: {player_score}')
        print(f'    Dealer hand: {dealer_hand}, current score: {dealer_score}')
        
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input('    Type "y" to get another card, "n" to pass: ')
            if should_continue == "y":
                player_hand.append(deal_card())
            else:
                game_over = True
    
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)
    
    print(f'    Final player hand: {player_hand}, final score: {player_score}')
    print(f'    Final dealer hand: {dealer_hand}, final score: {dealer_score}')
    
    if player_score > 21:
        return 'You went over. You lose!'
    elif dealer_score > 21:
        return 'Dealer went over. You win!'
    elif player_score == dealer_score:
        return 'Draw!'
    elif player_score == 0:
        return 'Blackjack! You win!'
    elif dealer_score == 0:
        return 'Dealer blackjack! You lose!'
    elif player_score > dealer_score:
        return 'You win!'
    else:
        return 'You lose!'

# Run the game
if __name__ == '__main__':
    result = play_blackjack()
    print(result)
