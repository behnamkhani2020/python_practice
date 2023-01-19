from User import User
import time,threading
class Games:
    def load_first_game(self,username):
        print('\n\t Welcome %s' % username)
        user = User(username)
        print("Loading your first game of RPS , be patient. ")
        try :
            for i in range(0,10):
                print('be patient ...')
                time.sleep(5)
        except KeyboardInterrupt:
            print('HA HA ,could\'nt be patient ... YOU WILL BE IN THE LOOSERS LIST FOREVER, unless you play the game and win.')
        winner_input_message = input("GOOD, you just won your first game, play next (Y)es (N)o : ")
