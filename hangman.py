'''

'''
import csv
import random




def generate_word(filename="Hangman 4K Database.csv"):
    """
    generates a random word from a csv file

    Parameters
    ----------
    filename : string
        name of CSV file where each row contains characters that
        form a single word

    Returns
    -------
    random_word : string
        a word from the csv file provided

    """
    
    with open("Hangman 4K Database.csv") as csvfile:
        data = csv.reader(csvfile)
        words_list = list()
        for row in data:
            words_list.extend(row)
    
    random_word = random.choice(words_list)
    return random_word.upper()




def prompt_guess(used_letters):
    '''
    prompts the user to enter an character and checks if string 
    is an used single character and part of the alphabet

    Returns
    -------
    guess : a string containing a single uppercase character

    '''
    
    invaild = True
    while invaild:
        guess = input("\nPlease enter a single unused alphabet as your guess: ")
        invaild = guess.upper() in used_letters or len(guess) != 1 or not guess.isalpha()
    return guess.upper()




def generate_incomplete_word(original_word, guessed_letters):
    '''
    takes the word to be guessed and the letters that have been guessed
        and generates a string with only the guessed letters visible

    Parameters
    ----------
    original_word : string
        the original word that the user is supposed to guess
    guessed_letters : string
        contains letters that have been guessed

    Returns
    -------
    word : string
        the original word where the letters that are not guessed
        are replaced by underscores

    '''
    
    word = str()
    for alphabet in original_word:
        if alphabet in guessed_letters:
            word = word + alphabet
        else:
            word = word + '_ '
    return word




def main():
    
    input('''Welcome to hangman\nPress enter to start''')
    incorrect_guesses = int(0)
    original_word = generate_word()
    word = original_word
    used_letters = str()
    guessed_letters = str()
    guess = str()
    
    while incorrect_guesses < 7:

        word = generate_incomplete_word(original_word, guessed_letters)
        
        
        if word.isalpha():
            print(f"You got the word.\nThe word was {word}")
            return
        
        
        print(f'''
----------------------------------------------------------------------------
\nYou have {incorrect_guesses} incorrect_guesses.''')
        print("Word:", word)
        
        
        guess = prompt_guess(used_letters)
        print("\n"*40)
        if guess in original_word:
            print(f"There is {guess} in the word")
            guessed_letters = guessed_letters + guess
        else:
            print(f"There is no {guess} in the word")
            incorrect_guesses += 1
        used_letters = used_letters + guess
        
        
        
    print('''\n\nYou ran out of guesses.\nThe word was''', original_word)





main()


'''
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
'''





