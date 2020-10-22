#!/usr/bin/env python
# coding: utf-8

# In[82]:


import random 


## Decrypt function defined so at the end, the user can have their word decoded

def decrypt(ciphertext):
    
    plaintext = ""
    
    for i in range (0, len(ciphertext)):
        
        if i % 2 == 0:
            
            plain_ascii = ord(ciphertext[i]) - 1
            
            plaintext = plaintext + chr(plain_ascii)
            
        elif i % 2 == 1:
            
            plain_ascii = ord(ciphertext[i]) + 1
            
            plaintext = plaintext + chr(plain_ascii)
            
    print(plaintext)
    
    
## Initialize all variables needed for the game to run

words = ['WHDSPQZ', 'XHO', 'TTDBFRT', 'QQJYF', 'ENQD', 'DNPK', 'CNTR', 'EHWHOD', 'TSVMOHOF', 'XNOCFQGTM']

attempts = 10

hangman_word = random.choice(words)

correct_guesses = []

incorrect_guesses = []

chosen_letters = list(hangman_word)



## Beginning of the game, introduction and set up follows ##

print("Hello, welcome to hangman! A word has been randomly selected for you to guess."
      "You are allowed 10 incorrect guesses. Good Luck!")


## This for loop adds a - for each letter in the scret word

for k in range(len(chosen_letters)):
    
    correct_guesses.append("-")
    
     
## This while loop runs as long as the user has more than 0 attempts left, the user will continue guessing letters until they
## either win (guess the word correctly with attempts remaining), or lose (attempts reach 0 before guessing word correctly)

while attempts >= 0:
        
    print(f"Mystery word: {correct_guesses}")
    print(f"{attempts} incorrect guesses remaining")
    print(f"Word bank: {incorrect_guesses}")
    
    guess = input("Guess a letter: ").upper()  
    
    
## find is a variable that allows the following for loop to check and see if a letter has already been guessed by the user
## if a letter is found to already be in the word, +1 will be applied to "find". If the letter is in the word and hasn't been
## guessed, the letter is added to the mystery word.

    find = 0
            
    for x in range(len(chosen_letters)):
            
        if chosen_letters[x] == guess:
            
            correct_guesses[x] = guess
            
            find += 1
            
## after checking the word for correct letters, if the letter has already been guessed (find=1) the program will return to the 
## while loop, if the letter is not found in the word AND hasn't already been guessed, an attempt is taken away and the letter
## is added to the word bank.
                
        elif x == (len(chosen_letters) - 1) and find == 0:
            
            if guess not in incorrect_guesses:
                
                attempts -= 1
                
                incorrect_guesses.append(guess)
                
                break
                
            else:
                
                break
                
## if the hangman_word matches the correct_guesses, the player wins and the word is decrypted to display the hidden word                
                
    if hangman_word == ''.join(correct_guesses) and attempts > 0:
        
        print(f"You won! Your encrypted word is: {hangman_word}.")
        
        decrypt(hangman_word)
        
        break
        
## if the player reaches 0 attempts, they lose and the game ends
        
    elif attempts == 0:
        
        print("Sorry. You lose!")
        
        break

