from User import User
import time
class Games:
    def load_first_game(self,username):
        print('\n\t Welcome %s' % username)
        user = User(username)
        print("Loading your first game of RPS , be patient : ")
        time.sleep(5)
        fake_input = input("enter a character to reset : ")