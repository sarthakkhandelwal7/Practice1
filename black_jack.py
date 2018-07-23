ask='y'
while(ask=='y'):
    c=0
    print('Press h for hit and s for stand')
    bet=int(input('Place your bet:'))
    values = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
    suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    new_deck = [[f'{v} of {s}',v] for s in suites for v in values]
    import random
    class BlackJack():


        def __init__(self):

            self.balance=100
            self.deck=new_deck
            random.shuffle(self.deck)
            self.dealer_cards=list()
            self.player_cards=list()
            self.check=0
            self.dealer_sum=0
            self.player_sum=0
            self.final_sum_p=0
            self.final_sum_d=0
            self.balance-=bet
            distribute()
            call_p=input('Do you want to hit or stand:')
            if(call_p=='h'):
                self.player()
            else:
                self.dealer()
        def sum_of_cards(self,check_list):
            total1=0
            total2=0
            i=0
            for card,val in check_list:
                if(type(val)==str and val!=ace):
                    total1+=10
                    total2+=10
                elif((val==ace)):
                    total+=1
                elif(val!=ace):
                    total2+=11
                else:
                    total1+=val
                    total2+=val
            return (total1,total2)   
        def player(self):
            while(call_p=='h'):
                (self.player_cards).append(self.deck[0])
                (self.deck).pop(0)
                self.player_sum=bj.sum_of_cards(self.player_cards)
                print(self.player_cards)
                if(self.player_sum[0]>21 and self.player_sum[1]>21):
                    print(f'Player Busts\nDealer won the game with sum of {self.final_sum_d}\nPlayer left with {self.balance}')
                    c+=1
            
                    break
            else:
                if(0<21-self.player_sum[0]<21-self.player_sum[1] ):
                    self.final_sum_p=self.player_sum[0]
                else:
                    self.final_sum_p=self.player_sum[1]
            if(call_p =='s'):
                self.dealer()
        def dealer(self):
            self.dealer_sum=bj.sum_of_cards(self.dealer_cards)
                        
            while (self.dealer_sum[0]<21 or self.dealer_sum[1]<21):
                (self.dealer_cards).append(self.deck[0])
                (self.deck).pop(0)
                self.dealer_sum=bj.sum_of_cards(self.dealer_cards)
                print(self.dealer_cards)
                if(self.dealer_sum[0]>21 and self.dealer_sum[1]>21):
                    self.balance+=(2*bet)
                    print(f'Dealer Busts\nPlayer won the game with sum of {self.final_sum_p}\nPlayer left with {self.balance}')
                    c+=1
                    break
            else:
                if(0<21-self.dealer_sum[0]<21-self.dealer_sum[1] ):
                    self.final_sum_d=self.dealer_sum[0]
                else:
                    self.final_sum_d=self.dealer_sum[1]    
    
    bj=BlackJack()
    
    def distribute():
        i=0
        l=0
        ip=0
        ide=1
        while(i<=1):
            i+=1
            (bj.dealer_cards).append(bj.deck[0])
            (bj.deck).pop(0)
        i=0
        while(i<=1):
            i+=1
            (bj.player_cards).append(bj.deck[0])
            (bj.deck).pop(0)
        for i in self.dealer_cards[ide][0]:
            ide+=1
            if(l==0):
                l+=1
                print('<Card hidden>')
            else:
                print(i)
        for k in self.player_cards[ip][0]:
            print(k)
            ip+=1
   
    if(c!=1):
        if(0<21-bj.final_sum_p<21-bj.final_sum_d):
            bj.balance+=(2*bet)
            print(f'Player won with sum of {bj.final_sum_p}\n total sum in bank is {bj.balance}')
        else:
            print()
            
    ask=input('Do you want to play Black Jack y or n:')
else:
    print('Thank You')