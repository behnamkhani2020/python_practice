import os,time,math,Welcome,Games

myWelcome = Welcome.Welcome()
myGame = Games.Games()

while True:
    os.system('clear')
    print(time.ctime())
    print(myWelcome.refresh,myWelcome.run)
    print (Welcome,myWelcome)
    myWelcome.welcome_message()
    myWelcome.game_interance_message()
    if myWelcome.refresh :
        continue
    elif myWelcome.run :
        myGame.load_first_game(myWelcome.username)
    else : 
        print("Goodby :>")
        break
        
