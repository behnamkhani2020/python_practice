from User import User
import time,threading
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
listener = keyboard.Listener(on_press=on_press)

def load_RPS():
    c = ''
    for i in range(0,3):
        if i == 2 : print('be carefull computer knows your choice everytime :>')
        user = input('lets play three rounds of (R)ock, (P)aper, (S)cissors, please select your choice by giving the first letter :')
        if user == "R" :
            c = c + "P"
            print("You lost this round, better lock next time :>") 
        elif user == "P" : 
            c = c + "S"
            print("You lost this round, better lock next time :>")
        elif user == "S" :
            c = c + "R"
            print("You lost this round, better lock next time :>")
        else : 
            raise TypeError
    if c == "RPS" :
        return True
    else :
        return False

class Games:
    def load_first_game(self,user):
        print('\n\t Welcome %s' % user.name)
        print("your honor : %d" % user.honor)
        print("Loading your first game of RPS , be patient. ")
        
        try :
            for i in range(0,2):
                print('be patient ... don\'t press ctrl+c ')
                time.sleep(1)
        except KeyboardInterrupt:
            print('HA HA ,could\'nt be patient ... YOU WILL BE IN THE LOOSERS LIST FOREVER, unless you play the game and win :>')
            losser_input_message = input("Would You ? (Y)es (N)o : ")
            return losser_input_message

        while(True):
            winner = load_RPS()
            if winner :
                print("Good, you won your first game :>")
                self.load_second_game(user)
            else :
                print("Bad, You will be added to losser list forever, unless you play again and win :>")
                losser_input_message = input("Would You ? (Y)es (N)o : ")
                if losser_input_message == 'Y' or losser_input_message == 'y' : 
                    continue
                else:
                    return False

    def load_second_game(self,user):
        listener.start()
        while(True):
            print("hurray for %s" % user.name)
            time.sleep(2)
