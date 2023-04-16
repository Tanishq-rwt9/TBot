# Introduction of bot
try:
 import random
 mylist = ["Stone","Paper","Scissor"]
 print('Hello friend')
 l=input('What is your name? ')
 print('Oh! Hello ',l)
 print('My name is Eva Your friend Robot')
 # First Input
 g = input('''Which game you want to play?
              1. Stone Paper Scissor 
              2. Make an Introduction for you''')
    # Elseif+input
 if g=='1':
    print('Ok You go first')
    u=input('Your Turn ')
    print(random.choice(mylist))
   # Elseif+Input
 print('Better luck next time\n 1:0')
 print('Thanks for trying my program')
 print('made by Tanishq <3')
except:
    print('Invalid')
