import os,time,math,Welcome,Games

myWelcome = Welcome.Welcome()
myGame = Games.Games()
from User import User

def chk_msg(msg):
    if msg == 'Y' or msg == 'y':
        return True
    else:
        return False

while True:
    os.system('clear')
    print(time.ctime())
    myWelcome.welcome_message()
    myWelcome.game_interance_message()
    if myWelcome.refresh :
        myWelcome.refresh = False
        myWelcome.run = False
        myWelcome.username = ''
        continue
    elif myWelcome.run :
        message = myGame.load_first_game(myWelcome.user)
        print(message)
        if chk_msg(message):
            pass
        else:
            print("Goodby :>")
            break
    else : 
        print("Goodby :>")
        break
        
