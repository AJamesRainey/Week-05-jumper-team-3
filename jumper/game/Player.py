class player():
    def __init__(self):
        self.guesses = []
        self.letter = ""

    def player_input(self):
        letter = input("What is the letter?: ")
        while True:
            letter = input("Enter a letter: ")
            if len(self.letter) < 2 and letter not in self.guesses:
                break
            self.guesses.append(self.letter)

