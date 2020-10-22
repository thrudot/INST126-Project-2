# INST126-Project-2

This code is a modified version of the famous "Hangman" game. A word will be randomly selected from the 'words' list and the user will need to guess a single letter at a time to guess the mystery word. They are only given 10 incorrect guesses until they lose. If they guess a letter correctly, it will display among the dashed lines ("-") which represent unknown letters. If the letter is successfully guessed before the 10 incorrect guesses, the secret word will display and be decoded into a real word using decrypt() function.

## Features
1. 10 incorrect guesses to guess the randomly selected word
2. Dashes that display how many letters are still unknown/length of word
3. Word bank that contains previosuly guessed incorrect guesses
4. Decrypts word and displays hidden word if the player wins
