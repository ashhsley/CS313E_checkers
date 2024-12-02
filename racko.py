# File: racko.py
# Description: A program that simulates the card and number game
# Rack-O. Players use the keyboard and take turns.
# Assignment Number: 9
#
# Name: Ali Pouamou
# EID:  ap63783
# Email: ali.chimoun@utexas.edu
# Grader: Risha
#
# On my honor, Ali Pouamou, this programming assignment is my own work
# and I have not provided this code to any other student.

import random


def main():
    """Play one game of Rack-O."""
    # Get the rack size, create the deck, and deal the initial racks.
    rack_size = prep_game()
    deck = list(range(1, 61))
    random.shuffle(deck)
    player = 0  # Player 1 corresponds to even numbers and Player 2 to odd ones
    player_1_rack = get_rack(deck, rack_size)
    player_2_rack = get_rack(deck, rack_size)
    discard = [deck.pop(0)]

    while not is_sorted(player_1_rack) and not is_sorted(player_2_rack):
        print(f"Player {player % 2 + 1}'s turn.")
        if player % 2 == 0:
            take_turn(deck, discard, player_1_rack)
        else:
            take_turn(deck, discard, player_2_rack)
        state_deck(deck, discard)
        player += 1

    if is_sorted(player_1_rack):
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')

    # CS303e students. Complete the main method to play
    # one complete game of Rack-O using the specified functions.


def prep_game():
    """Get ready to play 1 game.

    Show the instructions if the user wants to see them.
    Set the seed for the random number generator.
    Return the size of the rack to use.
    """

    print('----- Welcome to Rack - O! -----')
    if input('Enter y to display instructions: ') == 'y':
        instructions()
    print()
    random.seed(int(input('Enter number for initial seed: ')))
    rack_size = int(input('Enter the size of the rack to use. '
                          + 'Must be between 5 and 10: '))
    while not 5 <= rack_size <= 10:
        print(rack_size, 'is not a valid rack size.')
        rack_size = int(input('Enter the size of the rack to use. '
                              + 'Must be between 5 and 10: '))
    print()
    return rack_size


def instructions():
    """Print the instructions of the game."""
    print()
    print('The goal of the game is to get the cards in your rack of cards')
    print('into ascending order. Your rack has ten slots numbered 1 to 10.')
    print('During your turn you can draw the top card of the deck or take')
    print('the top card of the discard pile.')
    print('If you draw the top card of the deck, you can use that card to')
    print('replace a card in one slot of your rack. The replaced card goes to')
    print('the discard pile.')
    print('Alternatively you can simply choose to discard the drawn card.')
    print('If you take the top card of the discard pile you must use it to')
    print('replace a card in one slot of your rack. The replaced card goes')
    print('to the top of the discard pile.')


def take_turn(deck, discard, player_rack):
    """Take the player's turn.

    Give them the choice of drawing or taking the top card of the
    discard pile. If they draw they can replace a card or discard the
    draw. If they take the top card of the discard pile they must
    replace a card in their rack.
    """

    print('Your current rack', end='  ')
    print(player_rack)
    print('Top of discard pile', end='  ')
    print(discard[0])
    move = input('Enter d to draw anything else to take top of discard pile: ')
    print()
    if move == 'd':
        print('drew the', deck[0])
        choice = input('Enter p to place card, anything else to discard it: ')
        if choice == 'p':
            place_card(player_rack, deck.pop(0), discard)
        else:
            discard.insert(0, deck.pop(0))
    else:
        place_card(player_rack, discard.pop(0), discard)

    print('The rack after the turn', end='  ')
    print(player_rack)
    print()


def place_card(player_rack, new_card, discard):
    """Ask the player which card to replace in their rack.

    Replace it with the given new card. Place the card removed
    from the player's rack at the top of the discard pile.
    Error checks until player enters a card that is currently
    in their rack.
    """

    replace = int(input(f'Enter the card number to '
                        f'replace with the {new_card}: '))

    while not is_in_rack(player_rack, replace):
        print(f'{replace} is not in your rack.')
        replace = int(input(f'Enter the card number to '
                            f'replace with the {new_card}: '))

    i = index_card(player_rack, replace)
    discard.insert(0, player_rack[i])
    player_rack[i] = new_card


def is_sorted(rack):
    """Return if this rack is sorted in ascending order.

    CS303e assignment limitation:
    Do not create any new lists in this function.
    """

    for i in range(len(rack) - 1):
        if rack[i] > rack[i+1]:
            return False

    return True


def get_rack(deck, rack_size):
    """Deal the top rack_size cards of the deck into a new rack.

    The first card goes in the first slot, the second card goes in
    the second slot, and so forth. We assume len(deck) >= rack_size.
    Return the list of ints representing the rack.
    """

    rack = []
    for i in range(rack_size):
        rack.append(deck.pop(0))

    return rack


def is_in_rack(player_rack, the_card):
    """Check if a card is the player's rack

    Return True if it is and otherwise False
    """

    for card in player_rack:
        if card == the_card:
            return True

    return False


def index_card(player_rack, card):
    """Returns the index of a target card in a player's rack"""

    for i in range(len(player_rack)):
        if player_rack[i] == card:
            return i


def state_deck(deck, discard):
    """In the event the deck is empty

    Shuffle the discard pile and make a new deck of it
    Otherwise nothing happens
    """

    if not len(deck):
        random.shuffle(discard)
        while len(discard) > 1:
            deck.append(discard.pop(0))


main()