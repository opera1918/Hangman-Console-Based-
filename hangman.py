import random
import json
import os

figure = [
	'   -------------------\n   |      +----+     |\n   |      |    |     |\n   |           |     |\n   |           |     |\n   |           |     |\n   |           |     |\n   |    =========    |\n   -------------------\n',
    '   -------------------\n   |      +----+     |\n   |      |    |     |\n   |      O    |     |\n   |           |     |\n   |           |     |\n   |           |     |\n   |    =========    |\n   -------------------\n',
    '   -------------------\n   |      +----+     |\n   |      |    |     |\n   |      O    |     |\n   |      |    |     |\n   |           |     |\n   |           |     |\n   |    =========    |\n   -------------------\n',
    '   -------------------\n   |      +----+     |\n   |      |    |     |\n   |      O    |     |\n   |     /|    |     |\n   |           |     |\n   |           |     |\n   |    =========    |\n   -------------------\n',
    '   -------------------\n   |      +----+     |\n   |      |    |     |\n   |      O    |     |\n   |     /|\\   |     |\n   |           |     |\n   |           |     |\n   |    =========    |\n   -------------------\n',
    '   -------------------\n   |      +----+     |\n   |      |    |     |\n   |      O    |     |\n   |     /|\\   |     |\n   |     /     |     |\n   |           |     |\n   |    =========    |\n   -------------------\n',
    '   -------------------\n   |      +----+     |\n   |      |    |     |\n   |      O    |     |\n   |     /|\\   |     |\n   |     / \\   |     |\n   |           |     |\n   |    =========    |\n   -------------------\n',
	'   -------------------\n   |      +----+     |\n   |           |     |\n   |           |     |\n   |           |     |\n   |           |     |\n   |           |     |\n   |    =========    |\n   -------------------\n\n\n'
]

def move(direction, by):
    if direction == "W":
        return f"\033[{by}A"
    elif direction == "S":
        return f"\033[{by}B"
    elif direction == "D":
        return f"\033[{by}C"
    elif direction == "A":
        return f"\033[{by}D"
    
class Hangman:
    """
    Console based simple hangman game
    """
    initial = True
    already_used = False
    invalid_input = False
    incorrect_input = False
    def __init__(self, question) -> None:
        self.failed_attempts = 0
        self.word_guess_query = question[1]
        self.word_to_guess = question[0].upper()
        self.game_progress = list(u'\u2B1C' * len(self.word_to_guess))
    
    def game_title(self) ->  None:
        cwidth = os.get_terminal_size().columns
        print(u'\u001b[1;36m-+-+-+- CONSOLE BASED HANGMAN GAME USING PYTHON -+-+-+-'.center(cwidth))
        print(''.center(cwidth,'_'), end="\n\n")

    def display_question(self) -> None:
        print(u"\u001b[1;35m"+f"🔸 {self.word_guess_query}")

    def get_user_input(self):
        return input(" » ").upper()
    
    def is_invalid_letter(self, input_) -> bool:
        return (len(input_) >= 1 and not input_.isalpha())
    
    def find_indexes(self, letter):
        return [i for i, char in enumerate(self.word_to_guess) if letter == char]
    
    def update_progress(self, letter, indexes):
        for index in indexes:
            self.game_progress[index] = letter.upper()

    def print_game_status(self):
        if Hangman.incorrect_input == True:
            print(move("W", 2) + "\033[K" + "🔹 "+' '.join(self.game_progress) + '\t\t \u001b[1;31m(Incorrect input)\u001b[1;33m')
            Hangman.incorrect_input = False
            return
                   
        if Hangman.invalid_input == True:
            print(move("W", 2) + "\033[K" + "🔹 "+' '.join(self.game_progress) + '\t\t \u001b[1;31m(Invalid input)\u001b[1;33m')
            Hangman.invalid_input = False
            return
                  
        if Hangman.already_used == True:
            print(move("W", 2) + "\033[K" + "🔹 "+' '.join(self.game_progress) + '\t\t \u001b[1;31m(You already guessed it)\u001b[1;33m')
            Hangman.already_used = False
            return

        if Hangman.initial:
            print("\033[K" + "🔹 "+"\u001b[1;33m"+' '.join(self.game_progress))
            Hangman.initial = False
        else:
            print(move("W",2) + "\033[K" + "🔹 "+"\u001b[1;33m"+' '.join(self.game_progress))

    def play(self):
        global isGameOver
        print("\u001b[1;37m"+figure[-1][:-2] if exception_flage == False else "\u001b[1;37m"+figure[-1], end="\n\u001b[1;33m")
        while self.failed_attempts < len(figure)-1:
            self.print_game_status()
            
            user_input = self.get_user_input()

            if self.is_invalid_letter(user_input):
                print(move("W", 2))
                print("\033[K")
                Hangman.invalid_input = True
                continue
            
            if user_input in self.game_progress:
                print(move("W", 2))
                print("\033[K")
                Hangman.already_used = True
                continue
            
            if user_input in self.word_to_guess:
                indexes = self.find_indexes(user_input)
                self.update_progress(user_input, indexes)
                
                if u'\u2B1C' not in self.game_progress:
                    self.print_game_status()
                    print('\n\n   Correct! The word is: {0}'.format(self.word_to_guess))
                    break
            else:
                print(move("W", 12) + "\u001b[1;37m" + figure[self.failed_attempts] + move("S", 2), end="\n\u001b[1;33m")
                self.failed_attempts += 1
                Hangman.incorrect_input = True
                if self.failed_attempts >= len(figure)-1:
                    print("\u001b[1;31m\nGame Over!\u001b[0m\n")
                    isGameOver = True
                    return

if __name__ == '__main__':

    os.system('cls')
    with open('data.json', 'r') as file:
        quests = json.load(file)

    isGameOver = False
    exception_flage = False

    while len(quests):
        idx = random.choice(list(quests.keys()))
        hangman = Hangman(quests[idx])
        hangman.game_title()
        hangman.display_question()
        hangman.play()
        quests.pop(idx)

        exception_flage = True
        if isGameOver:
            break

        input("\n\u001b[1;32mPress Enter to continue...")
        os.system('cls')