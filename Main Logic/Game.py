word_to_guess="anisha"
guessed_word= ["_"] * len(word_to_guess)
attempts = 7
past_guess = []

def enter_single_char():
    userinput = input("Enter a letter:").lower()
    while True:
        if len(userinput) == 1 and userinput.isalpha():
            return userinput
        else:
            userinput = input("Invalid input. Please enter a single alphabet:").lower()

def validate_user_guess(guessed_word, word_to_guess, attempts, user_guess):
    print(guessed_word)
    word_to_guess2= list(word_to_guess)
    if user_guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess2[i] == user_guess:
                guessed_word[i] = user_guess
        return guessed_word,attempts
    else:
        attempts -= 1
        print(f"Sorry Wrong Guess! Attempts remaining:{attempts}")
        return guessed_word,attempts
'''
def multigameloop
def getrandomword'''

def track_past_guesses():
    global attempts
    global guessed_word
    while attempts > 0 and "_" in guessed_word:
        print(f"Word to guess:{''.join(guessed_word)}")
        print(f"Past guesses:{','.join(past_guess)}")
        print("Number of Attempts remaining:",attempts)

        user_guess = enter_single_char()
        if user_guess in past_guess:
            print("You already guessed that letter!")
            continue

        past_guess.append(user_guess)
        guessed_word,attempts= validate_user_guess(guessed_word, word_to_guess,attempts, user_guess)

    if "_" not in guessed_word or attempts == 0:
        print("Congratulations! You've successfully guessed the word:",''.join(guessed_word))
    else:
        print(f"Game Over! The correct word was {word_to_guess}")

track_past_guesses()








