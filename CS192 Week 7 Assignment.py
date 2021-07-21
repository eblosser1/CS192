#Hangman
name = input("What is your name? ")
print("Hello " + name, ", let's play a round of hangman!")
print("")
word = "programming"
guesses = ""
turns = 10
while turns > 0:
    failed = 0
    guess = input("Guess a character: ")
    guesses += guess
    for char in word:
        if char in guesses:
            print(char)
        else:
            failed += 1
    if failed == 0:
        print("You won!")
        break
    if guess not in word:
        turns -= 1
        print("Incorrect, try again.")
        print("You have", + turns, "guesses remaining.")
        if turns == 0:
            print("You lose.")
