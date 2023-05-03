# From fluent python Cap1

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    """A french deck of cards contains numbers from 2 to 10,
    J - Jack,
    Q - Queen,
    K - King,
    A - Ace,

    And the suits: Hearts, Diamonds, Clubs and Spades.
    """

    ranks = [str(n) for n in range(2, 11) + list("JQKA")]
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        """Initialized the deck of cards."""
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self) -> int:
        """Returns the length of the deck of cards.

        Returns:
            int: The length of the deck.
        """
        return len(self._cards)

    def __getitem__(self, position) -> Card:
        """Returns a card from the deck at the position argument.

        Args:
            position (_type_): The index in the cards array of the card requested.

        Returns:
            Card: The requested card.
        """
        return self._cards[position]


# Sorting is possible with the help of a sorting method

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card: Card) -> int:
    """Returns the "rank" of the card input
    This rank can be used to order the deck.

    Args:
        card (Card): The card that the rank is needed for

    Returns:
        int: The rank of the card
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# Sorting would look like this:
deck: FrenchDeck = FrenchDeck()

sorted_deck: list = sorted(deck, key=spades_high)
