import random
from player import Player


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"

    def select_gesture(self):
        self.chosen_gesture = random.randint(0, len(self.gestures)-1)
        print(f'{self.name} selects {self.gestures.get(self.chosen_gesture)}')