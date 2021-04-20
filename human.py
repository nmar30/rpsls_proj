from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("Please enter your name: ")

    def select_gesture(self):
        print(f'{self.name}s Turn')
        user_input = input("Enter your move: ")
        user_input = user_input.lower()
        if user_input == 'rock':
            self.chosen_gesture = 0
        elif user_input == 'paper':
            self.chosen_gesture = 1
        elif user_input == 'scissors':
            self.chosen_gesture = 2
        elif user_input == 'lizard':
            self.chosen_gesture = 3
        elif user_input == 'spock':
            self.chosen_gesture = 4
        else:
            print("Wrong Input!")
        print(f'{self.name} selects {self.gestures.get(self.chosen_gesture)}')
