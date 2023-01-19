

class Welcome:
    refresh = False
    run = False
    username= ''
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
            refresh_game_message = input('wrong answer, YOU WILL BE ADDED TO LOSER LIST FOREVER, unless you play again and win :>, Would YOU ? (Y)er (N)o :  ')
            if refresh_game_message == 'Y' or enter_game_answer == 'y' :
                self.refresh_game()
                return
            else :
                return
    
    def refresh_game(self):
        self.refresh = True
        return

    def run_game(self):
        self.run = True
        self.username = input('please submit a USERNAME : ')
        return
