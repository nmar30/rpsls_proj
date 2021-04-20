from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("Please enter your name: ")

    def select_gesture(self):
        print(f'{self.name}s Turn')
        selection = input("Enter your move: ")
        selection = selection.lower()
        if selection == 'rock':
            self.chosen_gesture = 0
        elif selection == 'paper':
            self.chosen_gesture = 1
        elif selection == 'scissors':
            self.chosen_gesture = 2
        elif selection == 'lizard':
            self.chosen_gesture = 3
        elif selection == 'spock':
            self.chosen_gesture = 4
        else:
            print("Wrong Input!")
        print(f'{self.name} selects {self.gestures.get(selection)}')
