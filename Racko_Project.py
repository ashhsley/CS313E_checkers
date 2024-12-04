import random
from collections import deque


class TreeRack:
    """
    This class will be auxiliary to check if our racks have heap property
    """

    def __init__(self, rack):
        """
        On this implementation the heap list is initialized with a value
        """
        self.rack = rack
        # self.rack.insert(0, 0)

    @property
    def size(self):
        """Returns the size of this heap"""
        return len(self.rack)

    def left(self, index):
        """Return the position of the left child node of a given index"""
        return 2 * index + 1

    def right(self, index):
        """Return the position of the right child node of a given index"""
        return (2 * index) + 2

    def is_leaf(self, index):
        """Returns true if the given index is a leaf node"""
        return index >= int((self.size - 1) / 2)

    def __str__(self):
        return str(self.rack)


def heap_invariant(tree, index):
    """Takes an object TreeRack as input, as well as a specified index and return
    True if it has heap property, False otherwise
    """

    # A Leaf node by itself satisfies the heap property
    if tree.is_leaf(index):
        return True

    # We then recursively check is the property holds for the current node and both subtrees

    l = tree.left(index)
    r = tree.right(index)
    if (tree.rack[index] <= tree.rack[l] and
            tree.rack[index] <= tree.rack[r] and
            heap_invariant(tree, l) and
            heap_invariant(tree, r)):
        return True

    return False


class Rack:
    def __init__(self, rack):
        self.rack = rack

    @property
    def size(self):
        return len(self.rack)

    def is_heap(self):
        """To check if our rack is sorted,
        we will implement an algorithm checking if a tree built off it has min_heap property"""
        t = TreeRack(self.rack)
        return heap_invariant(t, 0)

    def add(self, card):
        self.rack.append(card)

    def get_index(self, card):
        return self.rack.index(card)

    def get_card(self, index):
        return self.rack[index]

    def replace(self,new_card, index):
        self.rack[index] = new_card

    def is_in(self, card):
        return card in self.rack

    def __str__(self):
        return str(self.rack)


def main():
    """Play one game of Rack-O."""
    # Get the rack size, create the deck, and deal the initial racks.
    rack_size = prep_game()
    cards = list(range(1, 61))
    random.shuffle(cards)
    deck = deque(cards)
    player = 0  # Player 1 corresponds to even numbers and Player 2 to odd ones
    player_1_rack = Rack(get_rack(deck, rack_size))
    player_2_rack = Rack(get_rack(deck, rack_size))
    discard = deque([deck.popleft()])

    while not player_1_rack.is_heap() and not player_2_rack.is_heap():
        print(f"Player {player % 2 + 1}'s turn.")
        if player % 2 == 0:
            take_turn(deck, discard, player_1_rack)
        else:
            take_turn(deck, discard, player_2_rack)
        if not len(deck):
            random.shuffle(discard)
            while len(discard) > 1:
                deck.append(discard.popleft())
        player += 1

    if player_1_rack.is_heap():
        print('Player 1 wins!')
    else:
        print('Player 2 wins!')


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
    print('to satisfy a min-heap property. Your rack has ten slots numbered 1 to 10.')
    print('It means that given a slot number k, the cards at position 2k and 2k+1')
    print('must have smaller value than the one in k if within range')
    print()
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
            place_card(player_rack, deck.popleft(), discard)
        else:
            discard.appendleft(deck.popleft())
    else:
        place_card(player_rack, discard.popleft(), discard)

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

    while not player_rack.is_in(replace):
        print(f'{replace} is not in your rack.')
        replace = int(input(f'Enter the card number to '
                            f'replace with the {new_card}: '))

    i = player_rack.get_index(replace)
    discard.appendleft(player_rack.get_card(i))
    player_rack.replace(new_card, i)


'''Hi i got rid of the is_sorted method, is_in method, and the get_index method 
because those have functions built into python! I also changed the main method call. 
LMK if there r any issues!'''


def get_rack(deck, rack_size):
    """Deal the top rack_size cards of the deck into a new rack.

    The first card goes in the first slot, the second card goes in
    the second slot, and so forth. We assume len(deck) >= rack_size.
    Return the list of ints representing the rack.
    """

    rack = []
    for i in range(rack_size):
        rack.append(deck.popleft())

    return rack


if __name__ == "__main__":
    main()
