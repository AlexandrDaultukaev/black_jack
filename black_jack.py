import random
from art import logo
import time
#11 - ace
#10 - jack, queen, king
deck_of_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealers_hand = []
players_hand = []

def distribution_of_cards(p_hand, d_hand):
    """Distributes two cards to the player's hands"""
    for _ in range(2):
        d_hand.append(random.choice(deck_of_cards))
        p_hand.append(random.choice(deck_of_cards))

def take_card(hand):
    """Gives one card to hand if player want it"""
    while input("Do you want to take a card?(y/n): ") in ["yes", "y", "ye"]:
        hand.append(random.choice(deck_of_cards))
        print(hand)
    if 11 in hand:
        if input("You have Ace in your hand. Is it 1 or 11?(1, 11)") == "1":
            hand[hand.index(11)] = 1

def who_wins(p_hand, d_hand):
    """Makes desicion who wins"""
    if sum(p_hand) > 21:
        print("You lose!\n")
    elif sum(d_hand) > 21:
        print("You win!\n")
    elif sum(p_hand) == sum(d_hand):
        print("Draw!\n")
    elif sum(p_hand) > sum(d_hand):
        print("You win!\n")
    elif sum(p_hand) < sum(d_hand):
        print("You lose!\n")

def dealers_choice(d_hand):
    """Adds a card to dealers if the total of his cards is less than 17"""
    print("Dealer makes a desicion.")
    time.sleep(1)
    print("Dealer makes a desicion..")
    time.sleep(1)
    print("Dealer makes a desicion...")
    time.sleep(1)
    print("Dealer makes a desicion...[OK]")
    time.sleep(0.5)
    if sum(d_hand) < 17:
        d_hand.append(random.choice(deck_of_cards))

print(logo)
distribution_of_cards(players_hand, dealers_hand)
print("[" + "".join(str(dealers_hand[0])) + ", *]")
print(players_hand)
dealers_choice(dealers_hand)
take_card(players_hand)
print(f"Dealer's hand: {dealers_hand} = {sum(dealers_hand)}\nYour hand: {players_hand} = {sum(players_hand)}\n")
who_wins(players_hand, dealers_hand)


