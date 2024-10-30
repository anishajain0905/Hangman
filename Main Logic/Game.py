from random_word import RandomWords

# Create an instance of RandomWords
random_words_instance= RandomWords()

def enter_single_char():
    userinput = input("Enter a letter:").lower()
    while True:
        if len(userinput) == 1 and userinput.isalpha():
            return userinput
        else:
            userinput = input("Invalid input. Please enter a single alphabet:").lower()

def validate_user_guess(guessed_word, word_to_guess, attempts, user_guess):
    if user_guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == user_guess:
                guessed_word[i] = user_guess
        return guessed_word,attempts
    else:
        attempts -= 1
        print(f"Sorry Wrong Guess! Attempts remaining:{attempts}\n")
        return guessed_word,attempts

def get_random_word():
    return random_words_instance.get_random_word()

def game_loop():
    word_to_guess= get_random_word()

    guessed_word = ["_"] * len(word_to_guess)
    attempts = 8
    past_guesses = []

    while attempts > 0 and "_" in guessed_word:
        print(f"Word to guess:{''.join(guessed_word)}")
        print(f"Wrong guesses:{','.join(i for i in past_guesses if i not in guessed_word)}")
        print("Number of Attempts remaining:",attempts)

        user_guess = enter_single_char()
        if user_guess in past_guesses:
            print("You already guessed that letter!")
            continue

        past_guesses.append(user_guess)
        guessed_word,attempts= validate_user_guess(guessed_word, word_to_guess, attempts, user_guess)

    if "_" not in guessed_word :
        print("Congratulations! You've successfully guessed the word:",''.join(guessed_word))
    elif attempts == 0:
        print(f"Game Over! The correct word was {word_to_guess}. Better Luck next time!!")

'''def hangmanlook'''

game_loop()








