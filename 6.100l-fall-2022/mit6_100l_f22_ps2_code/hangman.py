# Problem Set 2, hangman.py
# Name: Pablo Silva
# Collaborators: N/A
# Time spent: 00:56:41

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word: # Does python interpret string as an iterable array..? We'll find out... (YES)
        if (char not in letters_guessed):
            return False
        
    return True
            


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for char in secret_word:
        if (char in letters_guessed):
            result += char
        else:
            result += "*"
    return result
        
            


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ""
    for char in string.ascii_lowercase: # Splendid hint!
        if (char in letters_guessed):
            continue 
        # Will only run if the letter isn't seen in the list
        result += char
    return result
    


def unique_letters(secret_word):
    """
    secret_word: string, the lowercase word the user is guessing

    returns: int, indicating the number of unique letters in secret_word
    """
    result = {"?", "."} # Arbitrary elements to indicate this is a set
    for char in secret_word:
        result.add(char)
    
    return len(result) - 2



def reveal_letter(secret_word, letters_guessed):
    """
    secret word: string, lowercase word the user is guessing
    word_progress: string, current progress on the secret word based on user guesses

    returns: char (string), unused letter revealed to the user
    """
    word_progress = get_word_progress(secret_word, letters_guessed)
    unguessed_letters = ""

    # Use range to compare with both lists
    for i in range(0, len(secret_word)):
        if (secret_word[i] != word_progress[i]):
            unguessed_letters += secret_word[i]
    
    return random.choice(unguessed_letters)
            
        


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 10
    length = len(secret_word)
    letters_guessed = []

    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {length} letters long.")

    # 2 outcomes
    while (guesses > 0 and has_player_won(secret_word, letters_guessed) == False):
        print(f"-----\nYou have {guesses} guesses left.")
        print(get_available_letters(letters_guessed))
        
        guess = input("Please guess a letter: ").lower() # Input can be both uppercase/lowercase
        
        # Input validation
        if (guess == "!" and with_help == True):
            if (guesses < 3):
                print("Oops! Not enough guesses left: ")
            else:
                guesses -= 3
                letter_revealed = reveal_letter(secret_word, letters_guessed)
                letters_guessed.append(letter_revealed)
                print(f"Letter revealed: {letter_revealed}")

        
        elif (guess.isalpha() == False or len(guess) != 1):
            print("Oops! That is not a valid letter. Please input a letter from the alphabet: ")

        elif (guess in letters_guessed):
            print("Oops! You have already guessed this letter.")

        elif (guess not in secret_word):
            # Consonants vs vowels (justice for y!)
            if (guess in ['a', 'e', 'i', 'o', 'u']):
                guesses -= 2
            else:
                guesses -= 1
            print("Oops! That letter is not in my word: ")
            letters_guessed.append(guess)

        else:
            # valid+correct guess
            print("Good guess: ")
            letters_guessed.append(guess)

        print(get_word_progress(secret_word, letters_guessed))
    
    print("-----") # Consistency with the game output
    
    if (guesses <= 0):
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    else:
        score = (guesses + 4 * unique_letters(secret_word)) + (3 * length)
        print("Congratulations you won!")
        print(f"Your total score for this game is: {score}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
