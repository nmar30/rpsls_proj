from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.player1 = self.select_player_type()
        self.player2 = self.select_player_type()
        self.win_matrix = [[-1, 1, 0, 0, 4],
                            [1, -1, 2, 3, 1],
                            [0, 2, -1, 2, 4],
                            [0, 3, 2, -1, 3],
                            [4, 1, 4, 3, -1]]

    def run_game(self):
        self.same_name_fix()
        i = 0
        while i < 3:
            self.player1.select_gesture()
            self.player2.select_gesture()
            self.compare_gestures()
            i += 1
        self.determine_winner()

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
        winner = self.win_matrix[self.player1.chosen_gesture][self.player2.chosen_gesture]
        if winner == self.player1.chosen_gesture:
            self.player1.score += 1
            print(f'******** {self.player1.name} Wins Round! ********')
        elif winner == self.player2.chosen_gesture:
            self.player2.score += 1
            print(f'******** {self.player2.name} Wins Round! ********')
        else:
            print("******** Tie Round! ********")

    def determine_winner(self):
        if self.player1.score == self.player2.score:
            print('--------------------------------')
            print('           Tie Game             ')
            print('--------------------------------')
        elif self.player1.score > self.player2.score:
            print('--------------------------------')
            print(f' {self.player1.name} Wins Game!')
            print('--------------------------------')
        else:
            print('--------------------------------')
            print(f' {self.player2.name} Wins Game!        ')
            print('--------------------------------')

    def same_name_fix (self):
        if self.player1.name == self.player2.name:
            self.player1.name += " 1"
            self.player2.name += " 2"