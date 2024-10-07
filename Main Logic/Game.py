word_to_guess="anisha"
print(len(word_to_guess) *"_")
def enter_single_char():
    while True:
        userinput = input("Enter a letter:").lower()
        if len(userinput) == 1 and userinput.isalpha():
            return userinput
        else:
            print("invalid input. Please enter a single alphabet")

user_guess= enter_single_char()

def track_past_guesses():
    past_guess= []
    attempts = 7
    guessed_word= "_" * len(word_to_guess)
    while attempts > 0 :
        print("Number of Attempts remaining:",attempts)
        enter_single_char()
        past_guess= [user_guess]
        if user_guess in word_to_guess:
             for i in len(word_to_guess):
                 if word_to_guess[i] == user_guess:
                     guessed_word[i] = user_guess
                     return guessed_word
        else:
            print("Sorry, Wrong guess!")
            attempts= (attempts - 1)









