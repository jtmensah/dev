import random
import string

from words import word


def get_valid_word(word):
        valid_word = random.choice(word)    #randomly chooses something from the list
        while "-" in valid_word or " " in valid_word:
            valid_word = random.choice(word)
        return valid_word.upper()

#print(get_valid_word(word))


def hangman():
    current_word = get_valid_word(word)
    word_letters = set(current_word)    #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    #letters already guessed by user
    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join(["a", "b", "cd"]) --> "a b cd"
        print("You have", lives, "lives left and you have used these letters: ", "".join(used_letters))

        #what current word is (ie W - RD)
        word_list = [letter if letter in used_letters else "-" for letter in current_word]
        print("Current word: ", "".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in current_word:
                word_letters.remove(user_letter)
            else:
                lives -= 1  #takes away a life if wrong
                print("Your letter", user_letter, "is not in word.")

        elif user_letter in used_letters:
            return "Sorry, you already used this letter! Try again."

        else:
            return "Invalid character! Try again."

    #gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("Sorry, you died! The word was", current_word)
    else:
        print("You guessed the word", current_word, "!!")

hangman()