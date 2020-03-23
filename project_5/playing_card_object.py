class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = list()
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        for s in suits:
            for r in ranks:
                self.cards.append(Card(r, s))

    def __str__(self):
        return f'{[f"{c.rank} of {c.suit}" for c in self.cards]}'


d = Deck()
print(d)
