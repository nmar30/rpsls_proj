from game import Game

if __name__ == '__main__':
    print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
    keep_playing = True
    game = Game()
    game.run_game()
    while keep_playing:
        x = input('Would you like to play another game? ')
        x = x.lower()
        if x == 'yes':
            game = Game()
            game.run_game()
            keep_playing = True
        elif x == 'no':
            print('Thanks for playing!')
            keep_playing = False
        else:
            print('Please enter Yes or No!')
