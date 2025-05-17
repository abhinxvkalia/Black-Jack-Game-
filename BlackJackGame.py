# %% [markdown]
# ## Black Jack Game

# %%
import random 

# %%
suits = ('Hearts','Diamonds','Spade','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'King':10,'Queen':10,'Ace':11}
playing = True 

# %%
class Card():
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit  

    def __str__(self):
        return self.rank +' of '+self.suit 

# %%
class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit)) 
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The Deck has' + deck_comp

# %%
class Hand():
    def __init__(self):
        self.cards_in_hand = []
        self.aces = 0
        self.value = 0
    
    def add_cards(self,card):
        self.cards_in_hand.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1 

    def adjust_for_aces(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# %%
class Chips():
    def __init__(self,total_chips = 100,bet_amount = 0):
        self.total_chips = total_chips
        self.bet_amount = bet_amount 
        

    def win_bet(self):
        self.total_chips += self.bet_amount

    def lose_bet(self):
        self.total_chips -= self.bet_amount

# %%
def take_bet(Chips):
    while playing:
        try:
            Chips.bet_amount = int(input("Enter your bet: "))
        except:
            print("Plz enter bet in integer form.")
        else:
            if Chips.bet_amount > Chips.total_chips:
                print("Sorry, your bet can't exceed", Chips.total_chips)
            else:
                break

# %%
def hit(deck,hand):
    hand.add_cards(deck.deal())
    hand.adjust_for_aces()

# %%
def hit_or_stand(deck, hand):
    global playing 
    while True:
        player_choice = input('Do you want to hit or stand: ').lower()

        if len(player_choice) == 0:
            print("Please enter a valid input.")
            continue

        if player_choice[0] == 'h':
            hit(deck, hand)
        elif player_choice[0] == 's':
            playing = False
        else:
            print('Please try again:')
            continue
        break

# %%
def show_some(player,dealer):
    print("\n Dealer's Hand:")
    print("\n 1st card is Hidden.")
    print(dealer.cards_in_hand[1])

    print("Player's Hand: ")
    print("\n Player Hand: ",*dealer.cards_in_hand,sep='\n')

def show_all(player,dealer):

    print("\n Player's Hand: ")
    for card in player.cards_in_hand:
        print(card)

    print("\n Dealer's Hand: ")
    for card in dealer.cards_in_hand:
        print(card)

    print("\n Value of Dealer's Hand: ",dealer.value)


# %%
def player_busts(player,dealer,chips): #arguments we passed here are player and dealer hand and chips
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

# %%
while True:
    print('Welcome to Black Jack.')

    new_deck = Deck()
    new_deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    for x in range(2):
        player_hand.add_cards(new_deck.deal())
        dealer_hand.add_cards(new_deck.deal())


    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        player_move = hit_or_stand(new_deck,player_hand)

        show_some(player_hand,dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break

    if player_hand.value >= 17:
        hit(new_deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        
        else:
            push(player_hand,dealer_hand)

    print("\nPlayer's winnings stand at: ",player_chips.total_chips)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

# %%



