suits = ["H", "C", "D", "S"]
ranks = ['2','3','4','5','6','7','8','9','10',"J","Q","K","A"]
scores = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,"J":10,"Q":10,"K":10,"A":1}

class Card(object):
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.suit + self.rank
import random

class Deck(object):
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def deal(self):
        x = self.deck.pop()
        return x
        
    def shuffle(self):
        random.shuffle(self.deck)

class Hand(object):
    
    def __init__(self):
        self.score = 0
        self.cards = []
        self.ace = False
        
    def draw_cards(self,card):
        self.cards.append(card)
        if card.rank == "A":
            self.ace = True
        self.score += scores[card.rank]
        
    def __str__(self,show):
            x = ""
            if show == "all":
                for card in self.cards:
                    x += card.__str__() + " "
            if show == "hide":
                for card in self.cards[:-1]:
                    x += card.__str__() + " "
            return x
    
    def calc_score(self,show):
        if show == "all":          
            if (self.ace == True) and (self.score < 12):
                y = self.score + 10
            else:
                y = self.score
        if show == "hide":
            y = "?"
        if show == "stand":
            if (self.ace == True) and (self.score < 12):
                y = self.score + 10
            elif (self.ace == True) and (self.score < 17) and (len(self.cards) == 2):
                y = self.score + 10
            else:
                y = self.score
        return y
        
def print_results():
    
    print "***"
    print "Player's hand: " + str(player_hand.__str__("all"))
    print "Player's score: " + str(player_hand.calc_score("all"))
    print "Dealer's hand: " + str(dealer_hand.__str__("hide")) + "with one card hidden"
    print "Dealer's score: " + str(dealer_hand.calc_score("hide"))
    
def hit_or_stand():
    x = ""
    while not (x == "s" or x == 'h'):
        x = raw_input("Hit or stand? Press s or h: ")
    if x == "s":
        stand()
    elif x == "h":
        hit()
        
def deal_cards():
    
    player_hand.draw_cards(deck.deal())
    player_hand.draw_cards(deck.deal())
    dealer_hand.draw_cards(deck.deal())
    dealer_hand.draw_cards(deck.deal())
    
    print_results()
    hit_or_stand()
    
def stand():
    
    while dealer_hand.calc_score("all") < 17:
        dealer_hand.draw_cards(deck.deal())
        print "***"
        print "Dealer's hand: " + str(dealer_hand.__str__("all"))
        #print "Dealer's score: " + str(dealer_hand.calc_score("all"))
    if dealer_hand.calc_score("all") >= 17:
        win()
    if dealer_hand.calc_score("all") >= 17:
        #print "Dealer's hand: " + str(dealer_hand.__str__("all"))
        print "Dealer's score: " + str(dealer_hand.calc_score("stand"))
        
def hit():
    
    if player_hand.calc_score("all") < 21:
        player_hand.draw_cards(deck.deal())
        print_results()
    if player_hand.calc_score("all") < 21:
        hit_or_stand()
    elif (player_hand.calc_score("all") == 21):
        win()
    elif player_hand.calc_score("all") > 21:
        win()
        
def win():
    
    if (dealer_hand.calc_score("all") > player_hand.calc_score("all")) and (dealer_hand.calc_score("all") < 21) and (player_hand.calc_score("all") < 21):
        print "Dealer won!"
    if dealer_hand.calc_score("all") >= 21:
        print "Dealer is busted! Player won!"
    if dealer_hand.calc_score("all") == player_hand.calc_score("all"):
        print "It's a draw!"
    if (player_hand.calc_score("all") > dealer_hand.calc_score("all")) and (player_hand.calc_score("all") < 21):
        print "Player won!"
    if player_hand.calc_score("all") == 21: 
        print "Player won!"
    if (player_hand.calc_score("all") > 21) and (dealer_hand.calc_score("all") < 21):
        print "Player is busted! Dealer won!"
        
#start game
game_on = True

while game_on == True:
   
    print "***"
    print "Welcome to Black Jack"
    player_hand = Hand()
    dealer_hand = Hand()
    deck = Deck()
    deck.shuffle()
    deal_cards()

    y = ""
    while not (y == "r" or y == "q"):
        y = raw_input("Restart or quit? Press r or q: ")
    if y == "r":
        game_on = True
    if y == "q":
        break

print "Bye bye."
