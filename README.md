# CS313E_Rack-O!!!

A simple card game with two players inspired by the Rack-O game from Milton Bradley (https://en.wikipedia.org/wiki/Rack-O).

The goal is to be the first to have a rack with cards that respect minimum heap invariant (https://en.wikipedia.org/wiki/Binary_heap).

Players both start with racks of equal lengths populated with cards ranging from 1 to 60 dealt from a randomly shuffled deck.


## <ins>Rack</ins> Object
**_class_** Rack(_[list]_)
Creates a Rack that will serve a holder for the cards of a player throughout an instance of the game.
A single and simple _list_ object is the sole property we need here. The list will also be the means used to display the racks

### size()
Returns the size of the current rack. In practice, the size is determined at the beginning and remains unchanged for the rest of the a game

### add(_card_)
Add a card to the rack. This method will be used only during the initialization of the game

### get_index(_card_)
Return the position of a specified card in the rack if it is present

### get_card(_index_)
Return a card at a given index

### replace(_new_card, index_)
Replace a card at a certain position by a new one

### is_in(_card_)
Checks if a card is indeed present in the rack

### is_heap()
To check if our rack is sorted, we will implement an algorithm checking if a tree built off it has min_heap property.
A recursive approach is implemented leading to a time complexity as **O(n)**


## <ins>TreeRack</ins> Object
_**class**_ TreeRack(_[list]_)
This class will be auxiliary to check if our racks have heap property

### size()
Returns the size of this heap; property of the class

### left(index)
Return the position of the left child node of a given index

### right(index)
Return the position of the right child node of a given index

### is_leaf(index)
Returns true if the given index is a leaf node and False if not


## <ins>Main Deck and Discard Pile</ins>
These two features are implemented using **deque** objects imported from the modue **collections**.

The collections module contains more specialized datatypes than the most common ones (list, dictionary, tuple, set,...). It's convenient since it doesn't require us to implement a stack object from scatch.
More about it can be found following the link below 
https://docs.python.org/3/library/collections.html#collections.deque

deque allows for quick and efficient addition as well as extraction of elements at both ends, which is perfect to implement a pile of cards

## <ins> Main Functions: How the game is played</ins>

### Preparatory Phase and Instructions
The game opens with the players being prompted messages to set the hyperparameters that are going to be used. Among those the _random seed_ that will affect the shuffling of the deck and thus the initial state of the each rack. The _size_ of the racks is also selected and has to range from 5 to 10. This is handled by a **_prep_game()_** function.
The players also have the option to display the instructions and rules. This part however may be skipped assuming they are acquainted enough with the mechanics of the game.

### Cards Dealing and Game Dynamics
Once everything is set, the 60 cards used are shuffled and the two decks are built one after the other with the number of cards afore agreed upon. The player then each take turns, starting with player 1 and go on until one of them reaches the heap goal. The _**take_turn(deck, discard, player_rack)**_ presents them with their different options. The game may be repeated at will with almost infinitely different initial setups. 


