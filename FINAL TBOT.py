import random
print('Welcome to robo world')
print('What do you want to do')

n=input("""         1. Play Rock Paper Scissor
         2. Make a 50 World random essay for you
         3. Nothing :> """)
if n=='1':
    b=input('First you ')
    sps=['Rock','Paper','Scissor']
    robo=(random.choice(sps))   
    print('YOU- ',b,' Robot- ',robo)
    if   b=='Rock' and robo=='Paper':
      print('Robot Wins🥳')
    elif b=='Paper' and robo=='Rock':
      print('You win🥳')
    elif b=='Rock' and robo=='Rock':
      print('Tie')


    elif b=='Paper' and robo=='Scissor':
      print('Robot wins🥳')
    elif b=='Scissor' and robo=='Paper':
      print('You win🥳')
    elif b=='Paper' and robo=='Paper':
      print('Tie')
    print('Bye')



elif n=='2':
    print('Ok here it is')
    mylist = ["""
You can do a lot of things in six weeks. You can lose 5 pounds. You can watch 6 episodes of “Grey’s Anatomy.” You can paint your kitchen. You can read “Americanah” and discuss it with your book club. You can drive to Montana to see your family.

On the other hand, there are some things that are almost impossible to do in six weeks. Like sell everything, find a new job, and move out of Texas.""", """
Nobody tells you to buckle up anymore. It isn’t necessary. Everyone just does it. But when seat belts first came along and the government was telling people to to use them, there were very controversial.

Why do we protest so much about things that are good for us? The human animals is so full of contradictions it’s hard to keep up with the nonsense we argue about. As Mr. Spock would say, “Humans are not logical.”""", """
I don’t miss writing checks to pay for everything and mailing them off in stamped envelopes to pay my bills. I don’t miss getting a whole chicken to cut up and then having to find someone foolish enough to eat the giblets. I don’t miss unairconditioned houses. I don’t miss twisting the handle on a mimeograph machine to make copies. I don’t miss those aspects of my youth. But I do miss my youth."""]

    a=(random.choice(mylist))   
    print(a)
    print('Bye')    
elif n=='3':
    print('OK')
else:
    print('BYE')

