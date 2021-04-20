from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.player1 = self.select_player_type()
        self.player2 = self.select_player_type()

    def run_game(self):
        i = 0
        while i < 3:
            self.player1.select_gesture()
            self.player2.select_gesture()
            self.compare_gestures()
            i += 1

    def welcome_message(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')

    def select_player_type(self):
        print('Please select a player type! Enter C for Computer or H for Human')
        while True:
            string = input("Enter Player Type:")
            string = string.lower()
            if string == 'c':
                return Computer()
            elif string == "h":
                return Human()
            print('Please enter C or H only!')

    def compare_gestures(self):
        print(f'{self.player1.chosen_gesture} vs. {self.player2.chosen_gesture}')
        if self.player1.chosen_gesture == self.player2.chosen_gesture:
            print("It's a tie!")
        