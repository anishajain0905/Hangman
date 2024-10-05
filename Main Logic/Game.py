Secret="Anisha"
def entersinglechar():
    while True:
        UserInput = input("Enter a letter:")
        if len(UserInput) == 1 and UserInput.isalpha():
            return(UserInput)
        else:
            print("invalid input. Please enter a single alphabet")

letter= entersinglechar()


