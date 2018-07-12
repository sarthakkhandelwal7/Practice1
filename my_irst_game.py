def introduction():
    intro='Hello, welcome to guess the number.'
    Rule_1='If your guess is within 10 of the number then its "WARM!"\nIf guess is further than 10 away from the number, its "COLD!"'
    Rule_2='If subsequent guess is closer to the number than the previous guess its "WARMER!"\nIf farther from the number than the previous guess, its "COLDER!"'
    print(intro +'\n'+ Rule_1+'\n'+Rule_2)


def codes():
    introduction()
    import random
    a= random.randint(1,101)
    store=0
    i=0
    while True:
        i+=1
        inp=int(input('Whats your guess:'))
        if(inp<0 or inp>100):
            print('Out of Bounds')
        if(a==inp):
            print(f'Hurrreee!!! you guesed it correct and took {i} turns')
            break
        elif(a-10<=inp<=a+10 and i==1):
            store=inp
            print('WARM')
        elif((a-10>inp or inp>a+10) and i==1):
            print('COLD')
            store=inp
        
        elif((abs(store-a)>abs(inp-a) ) and i>1):
            store=inp
            print('WARMER')
        elif(abs(store-a)<abs(inp-a)):
            print('COLDER')
            store=inp
                   
        
codes()        
