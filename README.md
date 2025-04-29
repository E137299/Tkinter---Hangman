# Tkinter: Hangman

![Hangman](images/hangman.png)

# Hangman 
Hangman is a popular word game in which one player (the "chooser") chooses a secret word and another  player (the "guesser") attempts to guess the word one letter at a time. If a guessed letter appears in the word,  all instances of it are revealed. If not, the guesser loses a chance. If the guesser figures out the secret word  before he or she runs out of chances, he or she wins. If not, the player who chose the word wins. Traditionally,  chances are tracked using a stick figure drawing of a person being hanged from a gallows. The figure is drawn  one body part at a time, and the guesser loses when the entire figure has been drawn.

## Details 
### Behavior 
**Gameplay** 

In our implementation of Hangman, the computer will take on the role of the "chooser" and the  human player will be the "guesser." The computer will secretly choose a word from a list (see  below) and show the player how many letters are in the word by displaying a sequence of  blanks (underscores). Then, the computer will begin asking for guesses. If the player guesses a  letter that is in the secret word, all blanks representing an instance of that letter should be  replaced by the letter. If the guessed letter is not in the word at all, the player should lose a  chance and a new part of the Hangman figure should appear. If the player guesses a letter he or  she has already guessed, he or she should not lose a chance, even if that letter is not in the  word. If the player guesses all letters in the word, he or she wins. If the Hangman figure is  completed, the player loses. In either case, the secret word should be revealed after the game  is over.

**Word Status:** 

As the game is played, the player should be shown the current guessed status of the secret word. Letters that have been correctly guessed should be shown in the correct locations.  Unguessed letters will appear as blanks. At the beginning of the game, no letters will have been  guessed, and the only information shown to the player will be a sequence of blanks, with one  blank for each letter in the secret word. As the player guesses letters correctly, blanks representing guessed letters should be replaced by those letters. So, for example, if the secret  word is "screwdriver" and the player has guessed 'e,' 's', 'r', and 'd,' the current word status  would be "s r e d r e r". 

**Chances/The Hangman:** 

The player will have six "chances" to guess the word. Guessing a correct letter does not cost a  chance. Each missed chance will cause a new piece of the Hangman to appear. The six pieces of  the Hangman are: head, body, left arm, right arm, left leg, right leg. 

**Game End:** 

The game can end in one of two ways: 
- If the player has guessed the complete secret word, he or she wins. 
- Otherwise, if the player has run out of chances and the complete Hangman has been drawn, the player loses.

In either case, when the game ends the host should stop asking for guesses. The host should  inform the player whether he or she won or lost, and the assistant should reveal the entire  secret word.
