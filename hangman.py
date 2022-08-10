import random
from words import words
import string

def get_valid_word(words):
    
    word = random.choice(words) # RANDOM WORD FROM THE LIST IN THE WORDS.PY
    
    while '-' in word or ' ' in word: # this is to miss the word containg a space or a dash
        word = random.choice(words)
        
    return word.upper()
        
        
def HangMan():
    word = get_valid_word(words)
    word_letters = set(word) ## the letters in the word       
    
    alphabet = set(string.ascii_uppercase)
    used_letters = set()## the user's guess
    lives = 10
    
    while len(word_letters) > 0 and lives > 0:
        ## used letters and how many lives left he has
        print('You have ', lives, 'lives left and you already guessed these letters: ', ' '.join(used_letters))
        
        ## showing the word depending on what letters he guessed
        word_pattern = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_pattern))
        
        
        user_letter = input('Guess a letter: ').upper()
        

        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives -= 1
                print('The letter is not in the world')
        elif user_letter in used_letters:
            print('You have already guessed this letter')    
            
        else:
            print('Invalid letter :(')
            
            
    if lives == 0:
        print('You lost, sorry better luck next time. The word is', word)
    else:
        print('Spot onnnnn, congrats you guessed the word !!!!')
    
    
HangMan()
    
    
    
    