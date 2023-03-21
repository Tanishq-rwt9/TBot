# Introduction of bot
print('Hello friend')
l=input('What is your name? ')
print('Oh! Hello ',l)
print('My name is Eva Your friend Robot')
# First Input
k=input('Wanna play a game with me?')
# Elseif + input
if k=='Yes':
    g = input('''Which game you want to play?
              1. Stone Paper Scissor 
              2. Make an Introduction for you''')
    # Elseif+input
if g=='1':
    print('Ok You go first')
    u=input('Your Turn')
   # Elseif+Input
    if u=='Scissor':
        print('Rock')
        print('Better luck next time')
        if u == 'Rock':
            print('Paper')
            print('Better luck next time')
        if u == 'Paper':
            print('Scissor')
            print('Better luck next time')
            print('Thanks for trying my program')
            print('made by Tanishq <3')
            if g=='2':
                print('lol')



