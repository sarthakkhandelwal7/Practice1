def display():
    print(f'{r3[0]} | {r3[1]} | {r3[2]}\n---------\n{r2[0]} | {r2[1]} | {r2[2]}\n---------\n{r1[0]} | {r1[1]} | {r1[2]}\n')


output_list=['x','o','x','o','x','o','x','o','x']
r1 = [' ',' ',' ']
r2 = [' ',' ',' ']
r3 = [' ',' ',' ']
c1=[1,4,7]
c2=[2,5,8]
c3=[3,6,9]
d1=[1,5,9]
d2=[3,5,7]
ch=[None,None,None,None,None,None,None,None,None]
count=0
ask=str(input("Do you want to play Y or N:"))
while(ask.lower()=='y'):
    if(count==0):
        display()
    for i in output_list:
        count+=1
        choice=int(input('Please enter your choice:'))
        print('\n')
        
        if(choice not in ch):
            ch[choice-1]=choice
            if(choice in range(1,4)):
                r1[choice-1]=i
                if((['x','x','x'] == r1) or (['o','o','o'] == r1) ):
                    if(count%2==0):
                        print('Player 2 won the game')
                        display()
                        break
                    else:
                        print('Player 1 won the game')
                        display()
                        break
            if(choice in range(4,7)):
                r2[choice-4]=i
                if((['x','x','x'] == r2) or (['o','o','o'] == r2) ):
                    if(count%2==0):
                        print('Player 2 won the game')
                        display()
                        break
                    else:
                        print('Player 1 won the game')
                        display()
                        break
            if(choice in range(7,10)):
                r3[choice-7]=i
                if((['x','x','x'] == r3) or (['o','o','o'] == r3) ):
                    if(count%2==0):
                        print('Player 2 won the game')
                        display()
                        break
                    else:
                        print('Player 1 won the game')
                        display()
                        break
            if(choice in c1):
                c1[c1.index(choice)]=i
                if((['x','x','x'] == c1) or (['o','o','o'] == c1) ):
                    if(count%2==0):
                        print('Player 2 won the game')
                        display()
                        break
                    else:
                        print('Player 1 won the game')
                        display()
                        break
            if(choice in c2):
                c2[c2.index(choice)]=i
                if((['x','x','x'] == c2) or (['o','o','o'] == c2) ):
                    if(count%2==0):
                        print('Player 2 won the game')
                        display()
                        break
                    else:
                        print('Player 1 won the game')
                        display()
                        break
            if(choice in c3):
                c3[c3.index(choice)]=i
                if((['x','x','x'] == c3) or (['o','o','o'] == c3) ):
                    if(count%2==0):
                        print('Player 2 won the game')
                        display()
                        break
                    else:
                        print('Player 1 won the game')
                        display()
                        break
            if(choice in d1):
                d1[d1.index(choice)]=i
                if((['x','x','x'] == d1) or (['o','o','o'] == d1) ):
                    if(count%2==0):
                        print('Player 2 won the game')
                        display()
                        break
                    else:
                        print('Player 1 won the game')
                        display()
                        break
            if(choice in d2):
                d2[d2.index(choice)]=i
                if((['x','x','x'] == d2) or (['o','o','o'] == d2) ):
                    if(count%2==0):
                        print('Player 2 won the game')
                        display()
                        break
                    else:
                        print('Player 1 won the game')
                        display()
                        break
            if(count<9):
                print('\n'*10)
                display()
            elif(count==9):
                print('Game is draw')
                display()
        else:
            print('You entered at this location choose new location')
    ask=str(input("Do you want to play Y or N:\n"))
                