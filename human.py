from player import Player


class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("Please enter your name: ")

    def select_gesture(self):
        print(f'{self.name}s Turn')
        print('Please select from the following Gestures:')
        i = 0
        while i < len(self.gestures):
            print(f'{[i]}. {self.gestures[i]}')
            i += 1
        selection = int(input("Gesture #:"))
        print(f'{self.name} selects {self.gestures[selection]}')
        self.chosen_gesture = self.gestures[selection]