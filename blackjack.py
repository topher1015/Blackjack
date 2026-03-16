import art
import random

"""
Simple Blackjack Game

This program allows a user to play a simplified game of Blackjack
against the computer (dealer). The goal is to get a score as close
to 21 as possible without going over.

Rules implemented:
- Number cards count as their value
- Face cards count as 10
- Ace can count as 11 or 1 depending on the score
- Blackjack (Ace + 10) is represented as 0 for easy comparison
"""

# Deck of possible card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """
    Randomly selects and returns a card from the deck.
    """
    return random.choice(cards)


def calculate_score(card_list):
    """
    Calculates the score of a hand.

    Rules:
    - If the hand has 21 with exactly 2 cards, it is considered Blackjack (returns 0).
    - If the score is over 21 and an Ace (11) exists, convert the Ace to 1.
    """
    score = sum(card_list)

    # Check for Blackjack (Ace + 10)
    if score == 21 and len(card_list) == 2:
        return 0

    # Adjust Ace value from 11 to 1 if score is over 21
    elif 11 in card_list and score > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


def compare(user_s, comp_s):
    """
    Compares the user score and computer score
    to determine the winner of the game.
    """

    print(f"Your final hand: {your_deck} final score: {calculate_score(your_deck)}")
    print(f"Computers final hand: {comp_deck} final score: {calculate_score(comp_deck)}")

    if user_s == comp_s:
        print("Draw! You tied!")

    elif comp_s == 0:
        print("You lose! Computer has blackjack!")

    elif user_s == 0:
        print("You win! You have blackjack!")

    elif comp_s > 21:
        print("You win! The computer went over 21!")

    elif user_s > 21:
        print("You lose! You went over 21!")

    elif user_s > comp_s:
        print("You win! Your score is higher!")

    else:
        print("You lose! Computer score is higher!")


# Controls whether the game continues running
restart = True

# Main game loop
while restart:

    # Initialize hands for each round
    your_deck = []
    comp_deck = []

    play = input("Do you want to play a game of blackjack? Type 'y' or 'n'. ").lower()

    if play == "n":
        restart = False
        print("Ok have a nice day!")
        break

    else:
        # Print game logo
        print(art.logo)

        # Deal two cards to player and dealer
        your_deck.append(deal_card())
        your_deck.append(deal_card())
        comp_deck.append(deal_card())
        comp_deck.append(deal_card())

        # Show player's cards and dealer's first card
        print(f"Your cards: {your_deck} current score: {calculate_score(your_deck)}")
        print(f"Computers first card: {comp_deck[0]}")

        # Player drawing loop
        draw_again = input("Type 'y' to get another card, type 'n' to pass. ").lower()

        while draw_again == "y":
            your_deck.append(deal_card())

            print(f"Your cards: {your_deck} current score: {calculate_score(your_deck)}")

            # Stop if player busts
            if calculate_score(your_deck) > 21:
                break

            draw_again = input("Type 'y' to get another card, type 'n' to pass. ").lower()

        # Dealer draws until score is at least 17 (standard blackjack rule)
        while calculate_score(comp_deck) < 17 and calculate_score(comp_deck) != 0:
            comp_deck.append(deal_card())

        # Compare final scores
        compare(calculate_score(your_deck), calculate_score(comp_deck))

        # Ask player if they want to play another round
        play_again = input("Would you like to restart the game? Enter 'y' or 'n'. ").lower()

        if play_again == "n":
            print("Goodbye")
            restart = False
        else:
            # Clear screen effect
            print("\n" * 20)
            print(art.logo)
            restart = True
