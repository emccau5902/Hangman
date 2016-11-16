import os
import random
def show_start_screen():
    print("  /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print(" / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("/ __  / (_| | | | | (_| | | | | | | (_| | | | |")
    print("\/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                   |___/                       ")
    print("")
    print("**************Let's play Hangman!**************")

def show_credits():
    print("   ___                         ___                 ")
    print("  / _ \__ _ _ __ ___   ___    /___\__   _____ _ __ ")
    print(" / /_\/ _` | '_ ` _ \ / _ \  //  //\ \ / / _ \ '__|")
    print("/ /_\\ (_| | | | | | |  __/ / \_//  \ V /  __/ |   ")
    print("\____/\__,_|_| |_| |_|\___| \___/    \_/ \___|_|   ")
    print("")
    print("*****************By Ethan McCauley*****************")
    
def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        full_path = path + "/" + f

        with open(full_path, "r") as file:
            print(str(i + 1) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice)

    return path + "/" + files[choice - 1]
    
def get_puzzle(file):
    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words[1:])
    
def check(word, solved, guesses):
    
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            return guess.upper()
        else:
            print("Error")

def display_board(solved, guesses, strikes):
    if strikes == 0:
        print("      _______  ")
        print("     |/      | ")
        print("     |         ")
        print("     |         ")
        print("     |         ")
        print("     |         ")
        print("  ___|___      ")
    if strikes == 1:
        print("      _______  ")
        print("     |/      | ")
        print("     |      (ツ)")
        print("     |         ")
        print("     |         ")
        print("     |         ")
        print("  ___|___      ")
    if strikes == 2:
        print("      _______  ")
        print("     |/      | ")
        print("     |      (ツ)")
        print("     |      \  ")
        print("     |         ")
        print("     |         ")
        print("  ___|___      ")
    if strikes == 3:
        print("      _______  ")
        print("     |/      | ")
        print("     |      (ツ)")
        print("     |      \ /")
        print("     |         ")
        print("     |         ")
        print("  ___|___      ")
    if strikes == 4:
        print("      _______  ")
        print("     |/      | ")
        print("     |      (ツ)")
        print("     |      \|/")
        print("     |       | ")
        print("     |         ")
        print("  ___|___      ")
    if strikes == 5:
        print("      _______  ")
        print("     |/      | ")
        print("     |      (ツ)")
        print("     |      \|/")
        print("     |       | ")
        print("     |      /  ")
        print("  ___|___      ")
    if strikes == 6:
        print("      _______   ")
        print("     |/      |  ")
        print("     |      (ツ) ")
        print("     |      \|/ ")
        print("     |       |  ")
        print("     |      / \ ")
        print("  ___|___       ")
    
              
    print(solved + "{" + guesses + "}")

def confirm():
    pass

def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)
    solved = "-" * len(word)

    guesses = ""
    strikes = 0
    limit = 6

    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)
    

    while word != solved and strikes < limit:
        letter = get_guess()
        if letter not in word:
            strikes += 1
        guesses += letter
        

        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)

        
    if word == solved:
        print("You win!")
    else:
        print("You lost.")
        print("The word was " + word)
        
def play_again():
    while True:
        answer = input("Would you like to play again?")

        if answer == 'no' or answer == 'n': 
            return False
    
        elif answer == 'yes' or answer == 'y':
            return True

        print("This was supposed to be a yes/no answer, not a short response.")

def main():
    show_start_screen()
    playing = True

    while playing:
        play()
        playing = play_again()

    show_credits()

# code execution begins here
if __name__ == "__main__":
    main()
