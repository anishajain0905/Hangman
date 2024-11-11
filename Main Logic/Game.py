import tkinter as tk
from random_word import RandomWords

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
    attempts = 7
    past_guesses = []
    while attempts > 0 and "_" in guessed_word:
        print(hangman_looks[7-attempts], "\n")
        print(f"Word to guess:{''.join(guessed_word)}")
        print(f"Wrong guesses:{','.join(i for i in past_guesses if i not in guessed_word)}")
        print("Number of Attempts remaining:",attempts,"\n")

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


hangman_looks = ['''
  |----------
  |
  |
  |
  |
  |
''',
'''
  |----------
  |         |
  |
  |
  |
  |
''',
'''
  |----------
  |         |
  |         ⬤
  |
  |
  |
''',
'''
  |----------
  |         |
  |         ⬤
  |         █
  |
  |
''',
'''
  |----------
  |         |
  |         ⬤
  |         █╲
  |
  |
''',
'''
  |----------
  |         |
  |         ⬤
  |        ╱█╲
  |
  |
''',
'''
  |----------
  |         |
  |         ⬤
  |        ╱█╲
  |          ╲ 
  |
''',
'''
  |----------
  |         |
  |         ⬤
  |        ╱█╲
  |        ╱ ╲ 
  |
''']

#game_loop()
class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.random_words_instance = RandomWords()
        self.word_to_guess = self.get_random_word()

        if not self.word_to_guess:
            print("Failed to retrieve a random word.")
            master.quit()

        self.guessed_word = ["_"] * len(self.word_to_guess)
        self.attempts = 8
        self.past_guesses = []

        # Create a canvas for the hangman drawing
        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()

        self.label = tk.Label(master, text=f"Word to guess: {''.join(self.guessed_word)}")
        self.label.pack()

        self.guess_label = tk.Label(master, text="Enter a letter:")
        self.guess_label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()
        self.entry.bind('<Return>', self.process_guess)

        self.attempts_label = tk.Label(master, text=f"Attempts remaining: {self.attempts}")
        self.attempts_label.pack()

        self.wrong_guesses_label = tk.Label(master, text="Wrong guesses: ")
        self.wrong_guesses_label.pack()

        self.draw_hangman()  # Draw the initial state

    def get_random_word(self):
        return self.random_words_instance.get_random_word()

    def draw_hangman(self):
        self.canvas.delete("all")  # Clear previous drawings

        # Coordinates for hangman parts
        hangman_stages = [
            [],  # Stage 0: No hangman drawn
            [(100, 40), (80, 60), (120, 60)],  # Head (drawn as a circle)
            [(100, 80), (100, 140)],  # Body
            [(100, 100), (60, 80)],  # Left Arm
            [(100, 100), (140, 80)],  # Right Arm
            [(100, 140), (60, 160)],  # Left Leg
            [(100, 140), (140, 160)],  # Right Leg
        ]

        # Draw hangman parts based on the number of attempts left
        for i in range(1, 8 - self.attempts + 1):  # Start from 1 to skip the initial state
            if i == 1:  # Draw the head
                self.canvas.create_oval(80, 20, 120, 60, outline='black', width=2)
            else:
                if i < len(hangman_stages):
                    for coords in hangman_stages[i]:
                        if i == 2:  # Draw the body
                            self.canvas.create_line(100, 60, 100, 140, fill='black', width=2)
                        else:
                            self.canvas.create_line(*coords, fill='black', width=2)

    def process_guess(self, event):
        user_guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)  # Clear the entry after getting the input

        if len(user_guess) == 1 and user_guess.isalpha():
            if user_guess in self.past_guesses:
                self.label.config(text="You already guessed that letter!")
                return

            self.past_guesses.append(user_guess)

            if user_guess in self.word_to_guess:
                # Update the guessed word with correct guesses
                for i in range(len(self.word_to_guess)):
                    if self.word_to_guess[i] == user_guess:
                        self.guessed_word[i] = user_guess
                self.label.config(text=f"Word to guess: {''.join(self.guessed_word)}")
            else:
                self.attempts -= 1
                self.attempts_label.config(text=f"Attempts remaining: {self.attempts}")
                self.wrong_guesses_label.config(text=f"Wrong guesses: {', '.join(self.past_guesses)}")
                self.draw_hangman()  # Update hangman drawing

            if "_" not in self.guessed_word:
                self.label.config(text="Congratulations! You've guessed the word!")
            elif self.attempts == 0:
                self.label.config(text=f"Game Over! The correct word was '{self.word_to_guess}'.")

        else:
            self.label.config(text="Invalid input. Please enter a single alphabet.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hangman Game")
    game = HangmanGame(root)
    root.mainloop()





