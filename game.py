from human import Human
from computer import Computer


class Game:
    def __init__(self):
        self.player1 = self.select_player_type()
        self.player2 = self.select_player_type()
        self.rpsls_table = [[-1, 1, 0, 0, 4],
                            [1, -1, 2, 3, 1],
                            [0, 2, -1, 2, 4],
                            [0, 3, 2, -1, 3],
                            [4, 1, 4, 3, -1]]


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
        winner = self.rpsls_table[self.player1.chosen_gesture][self.player2.chosen_gesture]
        # Declare the winner
        if winner == self.player1.chosen_gesture:
            print(self.player1.name, "WINS!!!")
        elif winner == self.player2.chosen_gesture:
            print(self.player2.name, "WINS!!!")
        else:
            print("TIE GAME")


        print(f'{self.player1.chosen_gesture} vs. {self.player2.chosen_gesture}')
        '''
        if self.player1.chosen_gesture == self.player2.chosen_gesture:
            print("It's a tie!")
        elif self.player1.chosen_gesture == 'Rock':
            if self.player2.chosen_gesture == 'Paper':
                self.player2.score += 1
                print(f'Paper covers Rock. {self.player2.name} Wins!')
            elif self.player2.chosen_gesture == 'Scissors':
                self.player1.score += 1
                print(f'Rock smashes Scissors. {self.player1.name} Wins!')
            elif self.player2.chosen_gesture == 'Lizard':
                self.player1.score += 1
                print(f'Rock crushes Lizard. {self.player1.name} Wins!')
            elif self.player2.chosen_gesture == 'Spock':
                self.player2.score += 1
                print(f'Spock vaporizes Rock. {self.player2.name} Wins!')
        '''