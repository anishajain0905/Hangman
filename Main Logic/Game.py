word_to_guess="anisha"
guessed_word= list("_" * len(word_to_guess))
guessed_word_normal=" "
print(guessed_word_normal.join(guessed_word))
def enter_single_char():
    userinput = input("Enter a letter:").lower()
    while True:
        if len(userinput) == 1 and userinput.isalpha():
            return userinput
        else:
            userinput = input("invalid input. Please enter a single alphabet")

user_guess= enter_single_char()
def validate_user_guess(guessed_word, word_to_guess):
    if user_guess in word_to_guess:
        for i in range (len(word_to_guess)):
            if word_to_guess[i] == user_guess:
                guessed_word[i] = user_guess
                return guessed_word
    else:
        print("Sorry, Wrong guess!")
        return []

'''def singlegameloop
word_to_guess="anisha"
print(len(word_to_guess) *"_")
def multigameloop

def getrandomword
    
def set'''

guessed_word= "_" * len(word_to_guess)
def track_past_guesses():
    past_guess= []
    attempts = 7
    guessed_word= "_" * len(word_to_guess)
    while attempts > 0 :
        past_guess= [user_guess]
        print("Number of Attempts remaining:",attempts)
        enter_single_char()
        validate_user_guess(guessed_word, word_to_guess)

track_past_guesses()








