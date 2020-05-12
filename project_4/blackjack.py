import random


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

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self):
        self.cards = [deck.cards[0], deck.cards[1]]
        self.bet = 1
        del deck.cards[:2]

    def __str__(self):
        return f'{[f"{c.rank} of {c.suit}" for c in self.cards]}'

    def tot(self):
        tot = 0
        ace = bool()
        for card in self.cards:
            if card.rank.isnumeric():
                tot += int(card.rank)
            elif card.rank == "Ace":
                ace = True
            else:                       # If the rank is King, Queen or Jack.
                tot += 10
        if ace:
            if tot < 11:
                tot += 11
            else:
                tot += 1
        return tot


class Dealer(Player):
    def __str__(self):
        return f'{[f"{self.cards[0].rank} of {self.cards[0].suit}", "Face down card"]}'

    def reveal_cards(self):
        return super().__str__()


deck = Deck()
deck.shuffle()

# Creates the dealer and the players

dealer = Dealer()
n_players = int(input("Number of players: "))
players = list()
for i in range(n_players):
    players.append(Player())
print()

# Shows the dealer's and the players' cards

print(f"Dealer's cards: {dealer}")
for player in players:
    n_player = players.index(player) + 1
    print(f"Player {n_player}'s cards: {player}")

# The round

for player in players:
    n_player = players.index(player) + 1
    while True:
        print()
        print(f"Player {n_player}'s cards: {player}")
        print(f"Player {n_player}'s total: {player.tot()}")

        if player.tot() == 21:
            player.bet *= 2.5
            print(f"Player {n_player} won this round! Total of bets {player.bet}")
            players[n_player - 1] = None
            break
        elif player.tot() < 21:
            print(f"Player {n_player}, choose one option: ")
            print("[1] Hit (You want more cards)")
            print("[2] Stay (You do not want more cards)")
            option = int(input("Enter your option: "))
            if option == 1:
                player.cards.append(deck.cards[0])
                del deck.cards[0]
            else:
                break
        else:
            dealer.bet += player.bet
            player.bet = 0
            print(f"Player {n_player} busted this round! Total of bets: {player.bet}")
            players[n_player - 1] = None
            break
print()

# The dealer's round

print(f"Dealer's cards: {dealer.reveal_cards()}")
print(f"Dealer's total: {dealer.tot()}")
while dealer.tot() <= 16:
    dealer.cards.append(deck.cards[0])
    del deck.cards[0]
    print(f"Dealer's cards: {dealer.reveal_cards()}")
    print(f"Dealer's total: {dealer.tot()}")
print()

# The results of the game

if dealer.tot() > 21:
    print("The dealer busted this round!\n")
    for player in players:
        if player is not None:
            n_player = players.index(player) + 1
            player.bet *= 2
            print(f"Player {n_player}'s total score ({player.tot()}) and total of bets ({player.bet})")
else:
    ranking = {"Dealer": dealer.tot()}
    for player in players:
        if player is not None:
            n_player = players.index(player) + 1
            if player.tot() > dealer.tot():
                player.bet *= 2
            else:
                dealer.bet += player.bet
                player.bet = 0
            print(f"Player {n_player} total of bets: {player.bet}")
            ranking[f"Player {n_player}"] = player.tot()
    sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
    print("\nResults...")
    for i in range(len(sorted_ranking)):
        name = sorted_ranking[i][0]
        score = sorted_ranking[i][1]
        print(f"{i+1}. {name} (Score: {score})")
