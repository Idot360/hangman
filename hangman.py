'''

'''
import csv
import random


def generate_word(filename="Hangman 4K Database.csv"):
    
    """
    Inputs:
      filename  - name of CSV file where each row contains characters that
                  form a single word
    Output:
      Returns a string containing a single word
    """
    
    with open("Hangman 4K Database.csv") as csvfile:
        data = csv.reader(csvfile)
        words_list = list()
        for row in data:
            words_list.append(row)
    
    random_word = random.choice(words_list)
    return random_word




'''
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
'''

def test_generate_word(limit):
    
    """
    Inputs:
      limit - an integer within 0-1000 that denotes how many times the
              function generate_word will be ran
    Output:
      None
      
    Will cause an error if generate_word is found to fail
    """
    for i in range(int(limit)):
        word = generate_word("Hangman 4K Database.csv")
        words_list = list()
        with open("Hangman 4K Database.csv") as csvfile:
            data = csv.reader(csvfile)
            for row in data:
                words_list.append(row)
        assert word in words_list


test_generate_word(1)




