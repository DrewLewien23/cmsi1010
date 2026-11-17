from dataclasses import dataclass
from random import shuffle
from collections import Counter

@dataclass(frozen=True)
class Card:
    suit: str
    rank: int

    def __post_init__(self):
        if self.suit not in ("S", "H", "D", "C"):
            raise ValueError("suit must be one of 'S', 'H', 'D', 'C'")
        if self.rank not in range(1, 14):
            raise ValueError("rank must be an integer between 1 and 13")

    def __str__(self):
        suit_str = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}[self.suit]
        rank_str = {1: "A", 11: "J", 12: "Q", 13: "K"}.get(
            self.rank, str(self.rank))
        return f"{rank_str}{suit_str}"


def standard_deck():
    return [Card(suit, rank) for suit in "SHDC" for rank in range(1, 14)]


def shuffled_deck():
    cards = standard_deck()
    shuffle(cards)
    return cards


def deal_one_five_card_hand():
    deck = shuffled_deck()
    return set(deck[:5])


def deal(number_of_hands, cards_per_hand):
    if not isinstance(number_of_hands, int):
        raise TypeError("hands must be int")
    if not isinstance(cards_per_hand, int):
        raise TypeError("cards per hand must be an int")
    if number_of_hands <= 0:
        raise ValueError("Need a postive number of hands")
    if cards_per_hand <= 0: 
        raise ValueError("Need a postive number of cards per hand")
    if number_of_hands * cards_per_hand > 52:
        raise ValueError("I don't have that many cards")
    deck = shuffled_deck()
    all_hands = []
    for i in range(number_of_hands):
        hand = set(deck[i*cards_per_hand  : (i+1)*cards_per_hand])
        all_hands.append(hand)
    return all_hands


def poker_classification(hand):
    if not isinstance(hand, set):
        raise TypeError('Hand must be a set for poker')
    if not all(isinstance(card, Card) for card in hand):
        raise TypeError('All items in hand must be Card objects')
    if len(hand) != 5:
        raise ValueError("Must have exactly 5 cards")

    ranks = tuple(sorted(card.rank for card in hand))
    suits = {card.suit for card in hand}

    is_flush = len(suits) == 1

    is_royal_ranks = (ranks == (1, 10, 11, 12, 13))
    is_straight = (ranks == tuple(
        range(ranks[0], ranks[0] + 5))) or is_royal_ranks

    counts = tuple(sorted(Counter(ranks).values(), reverse=True))

    if is_straight and is_flush:
        if is_royal_ranks:
            return "Royal Flush"
        return "Straight Flush"
    if counts == (4, 1):
        return "Four of a Kind"
    if counts == (3, 2):
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if counts == (3, 1, 1):
        return "Three of a Kind"
    if counts == (2, 2, 1):
        return "Two Pair"
    if counts == (2, 1, 1, 1):
        return "One Pair"

    return "High Card"