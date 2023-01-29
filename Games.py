from User import User
import time
from pynput import keyboard

def give_up(user,dishonor):
    give_up = input('or you can pay %d honors not to wait :>, Would You ? (Y) or (N) :'%dishonor)
    if give_up == "Y" or give_up == "y":
        user.honor = user.honor - dishonor
        return True
    else : 
        return False

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == "q":
            return
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    except KeyboardInterrupt:
        return

listener = keyboard.Listener(on_press=on_press)

def load_RPS(user):
    c = ''
    for i in range(0,3):
        if i == 2 : print('be carefull computer knows your choice everytime :>')
        print("round number %d"%i)
        print('be patient ... don\'t press ctrl+c ')
        if give_up(user,100) :
            break
        else:
            pass
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
            return False
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
            for i in range(0,3):
                print('be patient ... don\'t press ctrl+c ')
                if give_up(user,10) :
                    break
                else:
                    pass
                time.sleep(2)
        except KeyboardInterrupt:
            print('HA HA ,could\'nt be patient ... YOU WILL BE IN THE LOOSERS LIST FOREVER, unless you play the game and win :>')
            losser_input_message = input("Would You ? (Y)es (N)o : ")
            return losser_input_message
        
        print("Your honor now is %d"%user.honor)
        while(True):
            if give_up(user,100) :
                break
            else:
                pass
            winner = load_RPS(user)
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
        while(True):
            print("hurray for %s" % user.name)
            time.sleep(2)
