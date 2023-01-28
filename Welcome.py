from User import User
class Welcome:
    refresh = False
    run = False
    user = User("NEW")
    def welcome_message(self):
        print('\nHello there young adventurer . welcome to timewaste game by behnam khanyaghma :>')
        print('Warning !! if you are not a fresh young programmer just examining python LEAVE IMMIADIATELY :>\n')
        return

    def game_interance_message(self):
        enter_game_answer = input("Are you a fresh prograrmmer :: (Y)es (N)o  :")
        enter_game = False
        if enter_game_answer == 'Y' or enter_game_answer == 'y' : enter_game = True
        if enter_game : 
            self.run_game()
            return
        else :
            refresh_game_message = input('wrong answer, YOU WILL BE ADDED TO LOSER LIST FOREVER, unless you play again and win :>, Would YOU ? (Y)es (N)o :  ')
            if refresh_game_message == 'Y' or refresh_game_message == 'y' :
                self.refresh_game()
                return
            else :
                self.run = False
                self.user.name = 'NEW'
                return
    
    def refresh_game(self):
        self.refresh = True
        return

    def run_game(self):
        self.run = True
        self.user.name =  input('please submit a USER NAME : ')
        return
