# **Console-based Hangman Game (Python)**
This is a console-based implementation of the classic hangman game using Python. Players can guess letters to uncover a hidden word within a limited number of attempts.

[![Video Demo](https://i3.ytimg.com/vi/6-6Pttve7vM/maxresdefault.jpg)](https://www.youtube.com/watch?v=6-6Pttve7vM)

### How to Play 🎮
1. Run the Python script hangman.py.
1. You will be presented with a question or a clue related to the word to guess.
1. Enter a letter as your guess and press Enter.
1. The game will display the current state of the word, indicating if your guess was correct or incorrect.
1. If your guess is correct, the corresponding letters will be revealed in the word.
1. If your guess is incorrect, a part of the hangman figure will be displayed.
1.  Keep guessing letters until you either guess the word correctly or run out of attempts.
1. If you guess the word correctly, you win the game.
1. If you run out of attempts before guessing the word, you lose the game.
1. After each game, you can press Enter to continue to the next question.


### Game Controls 🕹️
Use the keyboard to enter a single letter as your guess.
Press Enter after entering your guess.


### Requirements 📃
Python 3.x


### Getting Started
Clone this repository to your local machine or download the files as a ZIP archive.
Open a terminal or command prompt and navigate to the project directory.

Run the following command to start the game:
```python hangman.py```


### Customizing Questions
The game uses a JSON file (data.json) to store the questions and associated words. You can customize the questions and words by modifying this file. Each question and word pair should be in the following format:
```
{
  "question_id": ["word_to_guess", "question"]
}
```
- question_id: A unique identifier for the question.
+ word_to_guess: The word that needs to be guessed.
- question: A clue or question related to the word.
+ You can add or remove question entries as desired.


### License

This project is licensed under the MIT License.
Feel free to contribute, report issues, or suggest improvements!
