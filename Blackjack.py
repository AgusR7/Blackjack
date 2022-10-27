from random import randint

# Blackjack Game

print ('Welcome to the Caligula casino')
print ('We want to know your name')
print ('So, can you tell us your name?')

name = input ('')
print ('Hmm, ok... ' + name + ', please, sit here and let the game begin')


class Blackjack:

    def __init__ (self):
    
        self.name = name
        card1 = randint (1, 10)
        card2 = randint (1, 10)
        card_list = [card1, card2]
        self.card_list = card_list
        card_totals = 0
        self.card_totals = card_totals

    def hit (self):
        print ('This are your actual cards: ')
        print (self.card_list)
        print ('Do you want another card? Type hit if you do so, and stand if you do not want more cards')
        choice = input ('')
        while choice != 'hit' and choice != 'stand':
            choice = input ('... please select hit or stand: ')
        if choice == 'hit':
            card3 = randint (1,10)
            self.card_list.append (card3)
            print ('Your new card is {card3}. You want another card? Type hit or stand'.format (card3 = card3))
            choice = ''
            choice = input ('')
            
            while choice != 'hit' and choice != 'stand':
                choice = input ('... please select hit or stand: ')
            if choice == 'hit':
                card4 = randint (1, 10)
                self.card_list.append (card4)
                print ('There you go, your fourth and last card is {card4}.'.format (card4 = card4))
            elif choice == 'stand':
                print ('Ok then, no more cards')

        elif choice == 'stand':
            print ('Ok then, no more cards.')
        print ('Your cards are: ' + str (self.card_list))

        total = 0
        for elements in range (0, len(self.card_list)):
            total = total + self.card_list [elements]
        if total >= 18:
            print ('Now this is your total: ' + str(total) + '. Nice hand!')
        elif total > 14 and total < 18:
            print ('Now this is your total: ' + str(total) + '. A quite decent hand!')
        else:
            print ('Now this is your total: ' + str(total) + '. Low odds of winning to be honest...')
        return ''


class Dealer:

    def __init__ (self):

        dealer_card1 = randint(1, 10)
        dealer_card2 = randint(1, 10)
        dealer_card_list = [dealer_card1, dealer_card2]
        self.dealer_card_list = dealer_card_list
        dealer_card_totals = 0
        self.dealer_card_totals = dealer_card_totals
    
    def dealer_cards (self):
        print ('The dealer cards are: ')
        print (self.dealer_card_list)
        total = 0
        for elements in range(0, len(self.dealer_card_list)):
            total = total + self.dealer_card_list [elements]
        print ('The sum of the dealer cards are ' + str(total))
        if total >= 17:
                print ('So here the dealer stands, with his total being ' + str(total))
        elif total <= 16:
             print ('The dealer has less than 16, then, he must draw a new card.')
             dealer_card3 = randint (1, 10)
             self.dealer_card_list.append (dealer_card3)
             print ('Now his cards are: ')
             print (self.dealer_card_list)
             total2 = 0
             for elements2 in range(0, len(self.dealer_card_list)):
                total2 = total2 + self.dealer_card_list [elements2]
             if total2 <= 16:
                print ('Again, the dealer has less than 16, he must draw his fourth and last card.')
                dealer_card4 = randint (1, 10)
                print (str (dealer_card4) + ' is his new card')
                self.dealer_card_list.append (dealer_card4)
    
        print ('To sumarise, his new cards are: ' + str(self.dealer_card_list))

        total =  0
        for elements in range (0, len(self.dealer_card_list)):
            total = total + self.dealer_card_list [elements]
        print ('The dealer total is: ' + str(total))
        print ('Remember! The winner is the highest number, but cannot overpass 21.')
        return ''
        

    
a = Blackjack().hit()
print (a)
b = Dealer().dealer_cards()
print (b)

