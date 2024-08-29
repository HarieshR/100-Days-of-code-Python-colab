import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "aadhithya"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

word = random.choice(word_list)
a = 0
blanks = []
for w in word:
    a += 1
    blanks.append("_")

def hangman(lives = 6):
    t ="_"
    if lives and t in blanks:

        inp = input("\nEnter a char of ur guess: ").lower()
        print(inp)
        print(word)
        word_lst = list(word)
        i = 0
        if inp in word_lst:
            while i < len(word_lst):
                if inp == word_lst[i]:
                    blanks[i] = inp
                i += 1
        else:
            lives -= 1

        print(blanks)
        print(stages[lives])

        hangman(lives)
    else:
        if lives:
            print("YAY!! U WON")
        else:
            print("HANGMAN")

hangman()

